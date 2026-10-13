from rest_framework import generics, mixins

from .models import Task
from .serializers import TaskSerializer


class TaskListCreateAPIView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    """Общий список задач и создание задачи по адресу /api/tasks/."""

    # GenericAPIView связывает выборку и сериализатор с логикой mixinов
    queryset = Task.objects.all().order_by("-created_at", "-id")
    serializer_class = TaskSerializer

    # ListModelMixin.list() сериализует весь queryset и возвращает Response 200
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # CreateModelMixin.create() проверяет входные данные, сохраняет задачу и
    # возвращает Response 201 ошибки сериализатора превращаются в Response 400
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TaskDetailAPIView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    """Получение, изменение и удаление одной задачи по ее pk."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = "pk"

    # RetrieveModelMixin.retrieve() находит объект и возвращает его с кодом 200
    # Если pk не существует, get_object() поднимает Http404, который DRF преобразует в ответ 404 с деталями ошибки.
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # UpdateModelMixin.update() требует полный набор обязательных полей
    # валидные данные сохраняются, а ошибки сериализатора дают ответ 40.
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # partial_update() включает partial=True клиенту достаточно передать
    # только изменяемые поля, но перед сохранением они проходят ту же валидацию
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    # DestroyModelMixin.destroy() удаляет объект и возвращает пустой ответ 204
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Mixinы формируют стандартные Response: 200 для чтения,изменения, 201 для
# создания, 204 для удаления, 400 для невалидных данных и 404 для неизвестного pk.
# 300 здесь не нужен; необработанный сбой приложения остается ошибкой сервера 500 и не маскируется под ошибку валидации.