"""
URL configuration for restapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.utils import extend_schema, extend_schema_view
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework import serializers
from rest_framework.authtoken.views import ObtainAuthToken

from rooms.openapi import ValidationErrorResponseSerializer


class TokenRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class TokenResponseSerializer(serializers.Serializer):
    token = serializers.CharField()


@extend_schema_view(
    post=extend_schema(
        tags=['Авторизация'],
        operation_id='auth_token_create',
        auth=[],
        description=(
            'Обменивает имя пользователя и пароль на токен '
            'Передавайте токен защищённым запросам как '
            'Authorization: Token <token>.'
        ),
        request=TokenRequestSerializer,
        responses={
            200: TokenResponseSerializer,
            400: ValidationErrorResponseSerializer,
        },
    ),
)
class DocumentedObtainAuthToken(ObtainAuthToken):
    pass


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rooms.urls')),
    path('api/', include('person.urls')),
    path(
        'api/auth/token/',
        DocumentedObtainAuthToken.as_view(),
        name='api-token-auth',
    ),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
]
