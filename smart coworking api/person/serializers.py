from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Profile
class RegistrationSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=50, write_only=True)
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = get_user_model()
        fields = ("id", "username", "password", "phone")
        read_only_fields = ("id",)

    def create(self, validated_data):
        phone = validated_data.pop("phone")
        user = get_user_model().objects.create_user(**validated_data)
        profile = user.profile
        profile.phone = phone
        profile.save(update_fields=["phone"])
        return user
class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    balance = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        read_only=True,
    )

    class Meta:
        model = Profile
        fields = ("id", "username", "phone", "balance")
        read_only_fields = ("id", "username", "balance")
