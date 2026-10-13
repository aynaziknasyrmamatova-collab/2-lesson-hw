from django.urls import path

from .views import TaskDetailAPIView, TaskListCreateAPIView


urlpatterns = [
    path("tasks/", TaskListCreateAPIView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailAPIView.as_view(), name="task-detail"),
]