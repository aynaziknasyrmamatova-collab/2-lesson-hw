from rest_framework import status
from rest_framework.exceptions import APIException


class BookingConflict(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "Статус бронирования изменился; обновите данные и повторите запрос."
    default_code = "booking_conflict"
