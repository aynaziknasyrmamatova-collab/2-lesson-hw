from datetime import timedelta

from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from tasks.models import Task


class TaskListAPITests(APITestCase):
    endpoint = "/api/tasks/"

    def test_admin_redirects_anonymous_user_to_login(self):
        response = self.client.get("/admin/")

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertIn("/admin/login/", response["Location"])

    def test_get_returns_tasks_as_json(self):
        task = Task.objects.create(title="Prepare report")

        response = self.client.get(self.endpoint, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["id"], task.id)
        self.assertEqual(response.data[0]["status"], Task.Status.PENDING)
        self.assertEqual(response.data[0]["priority"], 3)

    def test_post_creates_task(self):
        response = self.client.post(
            self.endpoint,
            {"title": "Prepare report", "description": "Quarterly results"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(response.data["title"], "Prepare report")
        self.assertIn("id", response.data)
        self.assertIn("created_at", response.data)
        self.assertIn("updated_at", response.data)

    def test_post_ignores_read_only_fields(self):
        response = self.client.post(
            self.endpoint,
            {
                "id": 100,
                "title": "Prepare report",
                "created_at": "2000-01-01T00:00:00Z",
                "updated_at": "2000-01-01T00:00:00Z",
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertNotEqual(response.data["id"], 100)
        self.assertNotEqual(response.data["created_at"], "2000-01-01T00:00:00Z")
        self.assertNotEqual(response.data["updated_at"], "2000-01-01T00:00:00Z")

    def test_post_rejects_short_title(self):
        response = self.client.post(
            self.endpoint, {"title": "abc"}, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("title", response.data)

    def test_post_rejects_numeric_title(self):
        response = self.client.post(
            self.endpoint, {"title": "12345"}, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("title", response.data)

    def test_post_rejects_priority_outside_range(self):
        response = self.client.post(
            self.endpoint,
            {"title": "Prepare report", "priority": 6},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("priority", response.data)
        self.assertEqual(
            response.data["priority"][0], "Приоритет должен быть от 1 до 5."
        )

    def test_get_retrieves_task_by_pk(self):
        task = Task.objects.create(title="Prepare report")

        response = self.client.get(f"{self.endpoint}{task.pk}/", format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], task.pk)

    def test_put_replaces_task_fields(self):
        task = Task.objects.create(title="Prepare report")

        response = self.client.put(
            f"{self.endpoint}{task.pk}/",
            {
                "title": "Review report",
                "description": "Updated details",
                "status": "in_progress",
                "priority": 4,
                "due_date": None,
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task.refresh_from_db()
        self.assertEqual(task.title, "Review report")
        self.assertEqual(task.priority, 4)

    def test_patch_updates_only_provided_fields(self):
        task = Task.objects.create(title="Prepare report", priority=2)

        response = self.client.patch(
            f"{self.endpoint}{task.pk}/",
            {"title": "Review report"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task.refresh_from_db()
        self.assertEqual(task.title, "Review report")
        self.assertEqual(task.priority, 2)

    def test_patch_validates_changed_fields(self):
        task = Task.objects.create(title="Prepare report")

        response = self.client.patch(
            f"{self.endpoint}{task.pk}/",
            {"priority": 6},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("priority", response.data)

    def test_put_rejects_invalid_data(self):
        task = Task.objects.create(title="Prepare report")

        response = self.client.put(
            f"{self.endpoint}{task.pk}/",
            {"title": "12345", "priority": 3},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("title", response.data)

    def test_delete_removes_task(self):
        task = Task.objects.create(title="Prepare report")

        response = self.client.delete(f"{self.endpoint}{task.pk}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(pk=task.pk).exists())

    def test_detail_methods_return_404_for_unknown_pk(self):
        detail_url = f"{self.endpoint}999/"
        requests = (
            self.client.get,
            self.client.put,
            self.client.patch,
            self.client.delete,
        )
        for request in requests:
            with self.subTest(method=request.__name__):
                if request in (self.client.put, self.client.patch):
                    response = request(
                        detail_url, {"title": "Valid task title"}, format="json"
                    )
                else:
                    response = request(detail_url)
                self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_rejects_past_due_date(self):
        past_due_date = (timezone.now() - timedelta(days=1)).isoformat()
        response = self.client.post(
            self.endpoint,
            {"title": "Prepare report", "due_date": past_due_date},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("due_date", response.data)

    def test_post_rejects_invalid_status(self):
        response = self.client.post(
            self.endpoint,
            {"title": "Prepare report", "status": "unknown"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("status", response.data)