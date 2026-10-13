from django.utils import timezone
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    # Явное поле оставляет проверку диапазона методу validate_priority ,вместо автоматических валидаторов модели, которые срабатывали бы раньше
    priority = serializers.IntegerField(default=3)

    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "description",
            "status",
            "priority",
            "due_date",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at")

    def validate_title(self, value):
        normalized_title = value.strip()
        if len(normalized_title) < 5:
            raise serializers.ValidationError(
                "Название должно содержать не менее 5 символов."
            )
        if normalized_title.isdigit():
            raise serializers.ValidationError(
                "Название не может состоять только из цифр."
            )
        return value

    def validate_priority(self, value):
        if not 1 <= value <= 5:
            raise serializers.ValidationError(
                "Приоритет должен быть от 1 до 5."
            )
        return value

    def validate(self, attrs):
        due_date = attrs.get("due_date")
        if due_date is not None and due_date < timezone.now():
            raise serializers.ValidationError(
                {"due_date": "Дедлайн не может быть в прошлом."}
            )
        return attrs