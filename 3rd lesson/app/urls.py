# Файл: папка_вашего_приложения/urls.py
from django.urls import path
from .views import TaskListAPIView  # Импортируем нашу View

urlpatterns = [
    # Пустой путь '', потому что префикс 'api/' уже добавился из главного urls.py
    # В итоге полный адрес будет: /api/tasks/
    path('tasks/', TaskListAPIView.as_view(), name='task-list'),
]
