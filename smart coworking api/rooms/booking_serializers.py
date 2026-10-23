from datetime import timedelta
from decimal import Decimal, ROUND_HALF_UP

from django.db import transaction
from django.utils import timezone
from rest_framework import serializers

from person.models import Profile

from .exceptions import BookingConflict
from .models import Booking, Room


class BookingSerializer(serializers.ModelSerializer):
    MAX_TOTAL_PRICE = Decimal("9999999999.99")
    room_name = serializers.CharField(source="room.name", read_only=True)
    starts_at = serializers.DateTimeField()
    ends_at = serializers.DateTimeField()

    class Meta:
        model = Booking
        fields = (
            "id",
            "room",
            "room_name",
            "starts_at",
            "ends_at",
            "hours",
            "price_per_hour",
            "total_price",
            "status",
            "created_at",
        )
        read_only_fields = (
            "id",
            "hours",
            "price_per_hour",
            "total_price",
            "status",
            "created_at",
        )

    def validate(self, attrs):
        starts_at = attrs.get("starts_at")
        ends_at = attrs.get("ends_at")
        if starts_at is None or ends_at is None:
            return attrs

        if starts_at < timezone.now():
            raise serializers.ValidationError(
                {"starts_at": "Нельзя бронировать на прошедшее время."}
            )
        if ends_at <= starts_at:
            raise serializers.ValidationError(
                {"ends_at": "Время окончания должно быть позже времени начала"}
            )

        duration = ends_at - starts_at
        if duration < timedelta(hours=1) or duration > timedelta(hours=12):
            raise serializers.ValidationError(
                {"ends_at": "Продолжительность бронирования должна быть от 1 до 12 часов"}
            )

        total_seconds = (
            Decimal(duration.days * 86400 + duration.seconds)
            + Decimal(duration.microseconds) / Decimal(1_000_000)
        )
        attrs["hours"] = (total_seconds / Decimal(3600)).quantize(
            Decimal("0.0001"),
            rounding=ROUND_HALF_UP,
        )
        return attrs

    def create(self, validated_data):
        user = self.context["request"].user
        hours = validated_data["hours"]

        with transaction.atomic():
            room = Room.objects.select_for_update().get(pk=validated_data["room"].pk)
            if not room.is_available:
                raise BookingConflict("Эта комната сейчас недоступна")

            overlapping_bookings = Booking.objects.filter(
                room=room,
                status__in=(Booking.Status.PENDING, Booking.Status.CONFIRMED),
                starts_at__lt=validated_data["ends_at"],
                ends_at__gt=validated_data["starts_at"],
            )
            if overlapping_bookings.exists():
                raise BookingConflict("Выбранное время уже занято.")

            profile = Profile.objects.select_for_update().get(user=user)
            total_price = room.price * Decimal(hours)
            total_price = total_price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
            if total_price > self.MAX_TOTAL_PRICE:
                raise serializers.ValidationError(
                    {"hours": "Сумма бронирования превышает допустимый предел"}
                )
            if profile.balance < total_price:
                raise serializers.ValidationError(
                    {"balance": "Недостаточно средств для бронирования"}
                )

            profile.balance -= total_price
            profile.save(update_fields=["balance"])
            return Booking.objects.create(
                user=user,
                room=room,
                hours=hours,
                starts_at=validated_data["starts_at"],
                ends_at=validated_data["ends_at"],
                price_per_hour=room.price,
                total_price=total_price,
            )


class BookingStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ("id", "status")
        read_only_fields = fields


class BookingCancelSerializer(serializers.Serializer):
    detail = serializers.CharField()