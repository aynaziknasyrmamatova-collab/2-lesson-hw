from rest_framework.routers import DefaultRouter
from django.urls import path

from .booking_views import (
    BookingCancelView,
    BookingConfirmView,
    BookingDetailView,
    BookingListCreateView,
)
from .views import RoomViewSet

router = DefaultRouter()
router.register("rooms", RoomViewSet, basename="room")

urlpatterns = router.urls + [
    path("bookings/", BookingListCreateView.as_view(), name="booking-list"),
    path(
        "bookings/<int:pk>/",
        BookingDetailView.as_view(),
        name="booking-detail",
    ),
    path(
        "bookings/<int:pk>/confirm/",
        BookingConfirmView.as_view(),
        name="booking-confirm",
    ),
    path(
        "bookings/<int:pk>/cancel/",
        BookingCancelView.as_view(),
        name="booking-cancel",
    ),
]
