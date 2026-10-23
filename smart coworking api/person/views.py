from django.shortcuts import get_object_or_404
from drf_spectacular.utils import OpenApiResponse, extend_schema, extend_schema_view
from rest_framework import generics, permissions

from .models import Profile
from .serializers import ProfileSerializer, RegistrationSerializer
from rooms.openapi import ErrorResponseSerializer, ValidationErrorResponseSerializer


@extend_schema_view(
    post=extend_schema(
        tags=["Пользователи"],
        operation_id="users_register",
        auth=[],
        description=(
            "Создаёт пользователя и профиль с указанным номером телефона. "
            "Новый внутренний баланс равен нулю. Пароль передаётся в JSON "
            "и сохраняется в виде хеша."
        ),
        request=RegistrationSerializer,
        responses={
            201: RegistrationSerializer,
            400: OpenApiResponse(
                response=ValidationErrorResponseSerializer,
                description="Ошибка валидации имени пользователя, телефона или пароля.",
            ),
        },
    ),
)
class RegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = (permissions.AllowAny,)


@extend_schema_view(
    get=extend_schema(
        tags=["Пользователи"],
        operation_id="profile_retrieve",
        description="Возвращает профиль пользователя из токена авторизации.",
        responses={
            200: ProfileSerializer,
            401: OpenApiResponse(
                response=ErrorResponseSerializer,
                description="Необходима авторизация по токену.",
            ),
        },
    ),
    put=extend_schema(
        tags=["Пользователи"],
        operation_id="profile_update",
        description=(
            "Обновляет номер телефона собственного профиля. Баланс и имя "
            "пользователя доступны только для чтения."
        ),
        request=ProfileSerializer,
        responses={
            200: ProfileSerializer,
            400: OpenApiResponse(
                response=ValidationErrorResponseSerializer,
                description="Ошибка валидации данных профиля.",
            ),
            401: OpenApiResponse(
                response=ErrorResponseSerializer,
                description="Необходима авторизация по токену.",
            ),
        },
    ),
    patch=extend_schema(
        tags=["Пользователи"],
        operation_id="profile_partial_update",
        description=(
            "Частично обновляет номер телефона собственного профиля. "
            "Баланс и имя пользователя доступны только для чтения."
        ),
        request=ProfileSerializer,
        responses={
            200: ProfileSerializer,
            400: OpenApiResponse(
                response=ValidationErrorResponseSerializer,
                description="Ошибка валидации данных профиля.",
            ),
            401: OpenApiResponse(
                response=ErrorResponseSerializer,
                description="Необходима авторизация по токену.",
            ),
        },
    ),
)
class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)

    def get_object(self):
        profile = get_object_or_404(self.get_queryset(), user=self.request.user)
        self.check_object_permissions(self.request, profile)
        return profile
