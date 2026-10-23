import json

from django.core.cache import cache
from django.db.models.deletion import ProtectedError
from drf_spectacular.utils import (
    OpenApiParameter,
    OpenApiResponse,
    extend_schema,
    extend_schema_view,
)
from rest_framework import status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import SAFE_METHODS, AllowAny, IsAdminUser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .cache import ROOM_LIST_CACHE_TIMEOUT, get_room_list_cache_key
from .models import Room
from .openapi import ErrorResponseSerializer, ValidationErrorResponseSerializer
from .serializers import RoomSerializer


@extend_schema_view(
    list=extend_schema(
        tags=["Комнаты"],
        operation_id="rooms_list",
        auth=[],
        description=(
            "Публично возвращает доступные комнаты. Администратор видит все "
            "комнаты. Результат содержит не более 10 записей на странице "
            "и кэшируется на 60 секунд."
        ),
        parameters=[
            OpenApiParameter(
                name="search",
                type=str,
                location=OpenApiParameter.QUERY,
                description="Поиск по названию комнаты без учёта регистра.",
            ),
            OpenApiParameter(
                name="capacity",
                type=int,
                location=OpenApiParameter.QUERY,
                description="Точная вместимость; положительное целое число",
            ),
            OpenApiParameter(
                name="ordering",
                type=str,
                location=OpenApiParameter.QUERY,
                enum=["price", "-price"],
                description="Сортировка по почасовой стоимости.",
            ),
            OpenApiParameter(
                name="page",
                type=int,
                location=OpenApiParameter.QUERY,
                description="Номер страницы (по 10 записей).",
            ),
        ],
        responses={
            200: RoomSerializer(many=True),
            400: OpenApiResponse(
                response=ValidationErrorResponseSerializer,
                description="Некорректная вместимость или параметр сортировки.",
            ),
        },
    ),
    retrieve=extend_schema(
        tags=["Комнаты"],
        operation_id="rooms_retrieve",
        auth=[],
        description=(
            "Получает сведения о комнате. Недоступные комнаты видны только "
            "администратору."
        ),
        responses={
            200: RoomSerializer,
            404: OpenApiResponse(
                response=ErrorResponseSerializer,
                description="Комната не найдена или недоступна посетителю",
            ),
        },
    ),
    create=extend_schema(
        tags=["Комнаты"],
        operation_id="rooms_create",
        description="Создаёт комнату. Требуются права администратора",
        request=RoomSerializer,
        responses={
            201: RoomSerializer,
            400: OpenApiResponse(
                response=ValidationErrorResponseSerializer,
                description="Поля комнаты не прошли валидацию",
            ),
            401: OpenApiResponse(
                response=ErrorResponseSerializer,
                description="Требуется авторизация администратора",
            ),
            403: OpenApiResponse(
                response=ErrorResponseSerializer,
                description="Пользователь не является администратором",
            ),
        },
    ),
    update=extend_schema(
        tags=["Комнаты"],
        operation_id="rooms_update",
        description="Полностью изменяет комнату. Требуются права администратора",
        request=RoomSerializer,
        responses={
            200: RoomSerializer,
            400: OpenApiResponse(
                response=ValidationErrorResponseSerializer,
                description="Поля комнаты не прошли валидацию",
            ),
            401: OpenApiResponse(response=ErrorResponseSerializer, description="Требуется авторизация администратора"),
            403: OpenApiResponse(response=ErrorResponseSerializer, description="Пользователь не является администратором"),
            404: OpenApiResponse(response=ErrorResponseSerializer, description="Комната не найдена"),
        },
    ),
    partial_update=extend_schema(
        tags=["Комнаты"],
        operation_id="rooms_partial_update",
        description="Частично изменяет комнату. Требуются права администратора",
        request=RoomSerializer,
        responses={
            200: RoomSerializer,
            400: OpenApiResponse(
                response=ValidationErrorResponseSerializer,
                description="Поля комнаты не прошли валидацию",
            ),
            401: OpenApiResponse(response=ErrorResponseSerializer, description="Требуется авторизация администратора"),
            403: OpenApiResponse(response=ErrorResponseSerializer, description="Пользователь не является администратором"),
            404: OpenApiResponse(response=ErrorResponseSerializer, description="Комната не найдена"),
        },
    ),
    destroy=extend_schema(
        tags=["Комнаты"],
        operation_id="rooms_destroy",
        description=(
            "Удаляет комнату. Требуются права администратора; комнату "
            "с бронированиями удалить нельзя"
        ),
        responses={
            204: OpenApiResponse(description="Комната удалена."),
            401: OpenApiResponse(response=ErrorResponseSerializer, description="Требуется авторизация администратора"),
            403: OpenApiResponse(response=ErrorResponseSerializer, description="Пользователь не является администратором"),
            404: OpenApiResponse(response=ErrorResponseSerializer, description="Комната не найдена"),
            409: OpenApiResponse(
                response=ErrorResponseSerializer,
                description="Нельзя удалить комнату с бронированиями",
            ),
        },
    ),
)
class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer

    def get_queryset(self):
        queryset = Room.objects.order_by("pk")
        if not self.request.user.is_staff:
            queryset = queryset.filter(is_available=True)

        search = self.request.query_params.get("search")
        if search:
            queryset = queryset.filter(name__icontains=search)

        capacity = self.request.query_params.get("capacity")
        if capacity is not None:
            try:
                capacity = int(capacity)
            except ValueError as exc:
                raise ValidationError(
                    {"capacity": "Укажите целое положительное число"}
                ) from exc
            if capacity < 1:
                raise ValidationError(
                    {"capacity": "Укажите целое положительное число"}
                )
            queryset = queryset.filter(capacity=capacity)

        ordering = self.request.query_params.get("ordering")
        if ordering is not None:
            if ordering not in {"price", "-price"}:
                raise ValidationError(
                    {"ordering": "Допустимые значения: price, -price"}
                )
            queryset = queryset.order_by(ordering, "pk")

        return queryset

    def list(self, request, *args, **kwargs):
        cache_key = get_room_list_cache_key(request)
        cached_data = cache.get(cache_key)
        if cached_data is not None:
            return Response(cached_data)

        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            response = self.get_paginated_response(serializer.data)
        else:
            serializer = self.get_serializer(queryset, many=True)
            response = Response(serializer.data)

        response_data = json.loads(JSONRenderer().render(response.data))
        cache.set(cache_key, response_data, ROOM_LIST_CACHE_TIMEOUT)
        response.data = response_data
        return response

    def get_permissions(self):
        permission_class = (
            AllowAny if self.request.method in SAFE_METHODS else IsAdminUser
        )
        return [permission_class()]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            self.perform_destroy(instance)
        except ProtectedError:
            return Response(
                {"detail": "Нельзя удалить комнату, у которой есть бронирования"},
                status=status.HTTP_409_CONFLICT,
            )
        return Response(status=status.HTTP_204_NO_CONTENT)
