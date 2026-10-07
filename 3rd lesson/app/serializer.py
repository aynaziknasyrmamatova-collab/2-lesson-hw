from rest_framework import serializers
from .models import Task
from django.utils import timezone
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=[
            'id','title','description','status',
            'priority','due_date','created_at', 'updated_at'
        ]
        read_only_fields=['id','created_at','updated_at']
    def validate_title(self,value):
        if len(value)<5:
            raise serializers.ValidationError("Название задачи не должно быть короче 5 символов ")
        if value.isdigit():
            raise serializers.ValidationError("Название задач не должно состоять только из цифр")
        return value
    def validate_priority(self,value):
        if value<1 or value>5 :
            raise serializers.ValidationError("Значение приоритета должно быть строго в диапазоне от 1 до 5")
        return value
    def validate(Self,attrs):
        due_date=attrs.get('due_date')
        if due_date and due_date < timezone.now():
            raise serializers.ValidationError(
                {"due_date": "Дата дедлайнв не может быть в прошлом"}
            )
        return attrs
    