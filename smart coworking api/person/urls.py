from django.urls import path

from .views import ProfileView, RegistrationView

urlpatterns = [
    path("register/", RegistrationView.as_view(), name="register"),
    path("profile/", ProfileView.as_view(), name="profile"),
]
