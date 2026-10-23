from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    capacity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name="Вместимость",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Стоимость одного часа",
    )
    is_available = models.BooleanField(default=True, verbose_name="Доступна")

    class Meta:
        verbose_name = "комната"
        verbose_name_plural = "комнаты"

    def __str__(self):
        return self.name


class Booking(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Ожидает подтверждения"
        CONFIRMED = "confirmed", "Подтверждено"
        CANCELLED = "cancelled", "Отменено"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="bookings",
        verbose_name="Пользователь",
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.PROTECT,
        related_name="bookings",
        verbose_name="Комната",
    )
    starts_at = models.DateTimeField(
        verbose_name="Начало бронирования",
    )
    ends_at = models.DateTimeField(
        verbose_name="Окончание бронирования",
    )
    hours = models.DecimalField(
        max_digits=6,
        decimal_places=4,
        validators=[MinValueValidator(1)],
        verbose_name="Количество часов",
    )
    price_per_hour = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Стоимость часа при бронировании",
    )
    total_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Итоговая стоимость",
    )
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING,
        verbose_name="Статус",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")

    class Meta:
        verbose_name = "бронирование"
        verbose_name_plural = "бронирования"
