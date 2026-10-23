from drf_spectacular.utils import (
    OpenApiParameter,
    OpenApiResponse,
    extend_schema,
    extend_schema_view,
)
from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework import status
from rest_framework.exceptions import APIException, ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from person.models import Profile

from .booking_serializers import BookingSerializer, BookingStatusSerializer
from .models import Booking
from .openapi import ErrorResponseSerializer, ValidationErrorResponseSerializer


@extend_schema_view(
    get=extend_schema(
        tags=["Бронирования"],
        operation_id="bookings_list",
        description="Возвращает только бронирования текущего пользователя",
        parameters=[
            OpenApiParameter(
                name="room",
                type=int,
                location=OpenApiParameter.QUERY,
                description="Фильтр по идентификатору комнаты",
            ),
            OpenApiParameter(
                name="search",
                type=str,
                location=OpenApiParameter.QUERY,
                description="Поиск по названию комнаты",
            ),
            OpenApiParameter(
                name="ordering",
                type=str,
                location=OpenApiParameter.QUERY,
                enum=[
                    "starts_at",
                    "-starts_at",
                    "created_at",
                    "-created_at",
                    "total_price",
                    "-total_price",
                    "hours",
                    "-hours",
                ],
                description="Поле сортировки; префикс - задаёт обратный порядок",
            ),
            OpenApiParameter(
                name="status",
                type=str,
                location=OpenApiParameter.QUERY,
                enum=[status for status, _ in Booking.Status.choices],
                description="Фильтр по статусу бронирования",
            ),
            OpenApiParameter(
                name="page",
                type=int,
                location=OpenApiParameter.QUERY,
                description="Номер страницы",
            ),
        ],
        responses={
            200: BookingSerializer(many=True),
            401: OpenApiResponse(
                response=ErrorResponseSerializer,
                description="Необходима авторизация по токену",
            ),
            400: OpenApiResponse(
                response=ValidationErrorResponseSerializer,
                description="Некорректный идентификатор фильтра или сортировки",
            ),
        },
    ),
    post=extend_schema(
        tags=["Бронирования"],
        operation_id="bookings_create",
        description=(
            "Создаёт ожидающее подтверждения бронирование. Укажите комнату "
            "и временные отметки starts_at и ends_at в ISO 8601. "
            "Продолжительность — от 1 до 12 часов. Стоимость вычисляется "
            "сервером и списывается с баланса в одной транзакции"
        ),
        request=BookingSerializer,
        responses={
            201: BookingSerializer,
            400: OpenApiResponse(
                response=ValidationErrorResponseSerializer,
                description=(
                    "Ошибки полей/интервала, недоступная или занятая комната, "
                    "недостаточный баланс или превышение максимальной стоимости"
                ),
            ),
            409: OpenApiResponse(
                response=ErrorResponseSerializer,
                description="Интервал уже занят",
            ),
            401: OpenApiResponse(
                response=ErrorResponseSerializer,
                description="Необходима авторизация по токену",
            ),
        },
    ),
)
class BookingListCreateView(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        queryset = (
            Booking.objects.filter(user=self.request.user)
            .select_related("room")
            .order_by("pk")
        )

        booking_status = self.request.query_params.get("status")
        valid_statuses = {value for value, _ in Booking.Status.choices}
        if booking_status is not None:
            if booking_status not in valid_statuses:
                raise ValidationError(
                    {
                        "status": (
                            "Допустимые значения: pending, confirmed, cancelled."
                        )
                    }
                )
            queryset = queryset.filter(status=booking_status)

        room = self.request.query_params.get("room")
        if room is not None:
            try:
                room_id = int(room)
            except ValueError as exc:
                raise ValidationError(
                    {"room": "Укажите корректный идентификатор комнаты"}
                ) from exc
            if room_id < 1:
                raise ValidationError(
                    {"room": "Укажите корректный идентификатор комнаты"}
                )
            queryset = queryset.filter(room_id=room_id)

        search = self.request.query_params.get("search")
        if search:
            queryset = queryset.filter(room__name__icontains=search)

        ordering = self.request.query_params.get("ordering")
        allowed_orderings = {
            "starts_at",
            "-starts_at",
            "created_at",
            "-created_at",
            "total_price",
            "-total_price",
            "hours",
            "-hours",
        }
        if ordering is not None:
            if ordering not in allowed_orderings:
                raise ValidationError(
                    {
                        "ordering": (
                            "Допустимые значения: starts_at, -starts_at, "
                            "created_at, -created_at, total_price, -total_price, "
                            "hours, -hours."
                        )
                    }
                )
            queryset = queryset.order_by(ordering, "pk")

        return queryset


class BookingConflict(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "Статус бронирования изменился; обновите данные и повторите запрос"
    default_code = "booking_conflict"


@extend_schema(
    tags=["Бронирования"],
    operation_id="bookings_retrieve",
    description="Получает бронирование только текущего пользователя",
    responses={
        200: BookingSerializer,
        401: OpenApiResponse(
            response=ErrorResponseSerializer,
            description="Требуется авторизация.",
        ),
        404: OpenApiResponse(
            response=ErrorResponseSerializer,
            description="Бронирование не найдено.",
        ),
    },
)
class BookingDetailView(generics.RetrieveAPIView):
    serializer_class = BookingSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user).select_related("room")


@extend_schema(
    tags=["Бронирования"],
    operation_id="bookings_confirm",
    description=(
        "Подтверждает ожидающее бронирование. Доступно только администраторам; "
        "доступность комнаты и отсутствие пересечений проверяются повторно"
    ),
    request=None,
    responses={
        200: BookingStatusSerializer,
        401: OpenApiResponse(
            response=ErrorResponseSerializer,
            description="Требуется авторизация администратора",
        ),
        403: OpenApiResponse(
            response=ErrorResponseSerializer,
            description="Только администратор может подтвердить бронирование",
        ),
        404: OpenApiResponse(
            response=ErrorResponseSerializer,
            description="Бронирование не найдено",
        ),
        409: OpenApiResponse(
            response=ErrorResponseSerializer,
            description="Бронирование уже обработано или интервал недоступен",
        ),
    },
)
class BookingConfirmView(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def post(self, request, pk):
        with transaction.atomic():
            booking = get_object_or_404(
                Booking.objects.select_for_update().select_related("room"),
                pk=pk,
            )
            if booking.status != Booking.Status.PENDING:
                raise BookingConflict("Подтвердить можно только ожидающее бронирование")

            room = booking.room
            if not room.is_available:
                raise BookingConflict("Комната больше недоступна")

            has_conflict = Booking.objects.filter(
                room=room,
                status__in=(Booking.Status.PENDING, Booking.Status.CONFIRMED),
                starts_at__lt=booking.ends_at,
                ends_at__gt=booking.starts_at,
            ).exclude(pk=booking.pk).exists()
            if has_conflict:
                raise BookingConflict("Выбранное время уже занято другим бронированием")

            booking.status = Booking.Status.CONFIRMED
            booking.save(update_fields=["status"])

        return Response(BookingStatusSerializer(booking).data)


@extend_schema(
    tags=["Бронирования"],
    operation_id="bookings_cancel",
    description=(
        "Отменяет собственное ожидающее или подтверждённое бронирование "
        "и возвращает списанную сумму на баланс пользователя."
    ),
    request=None,
    responses={
        200: BookingStatusSerializer,
        401: OpenApiResponse(
            response=ErrorResponseSerializer,
            description="Требуется авторизация.",
        ),
        404: OpenApiResponse(
            response=ErrorResponseSerializer,
            description="Собственное бронирование не найдено",
        ),
        409: OpenApiResponse(
            response=ErrorResponseSerializer,
            description="Бронирование уже отменено",
        ),
    },
)
class BookingCancelView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk):
        with transaction.atomic():
            booking = get_object_or_404(
                Booking.objects.select_for_update().filter(user=request.user),
                pk=pk,
            )
            if booking.status == Booking.Status.CANCELLED:
                raise BookingConflict("Бронирование уже отменено")

            profile = Profile.objects.select_for_update().get(user=request.user)
            profile.balance += booking.total_price
            profile.save(update_fields=["balance"])

            booking.status = Booking.Status.CANCELLED
            booking.save(update_fields=["status"])

        return Response(BookingStatusSerializer(booking).data)
