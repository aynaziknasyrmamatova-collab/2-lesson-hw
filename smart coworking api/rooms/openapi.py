from rest_framework import serializers


class ErrorResponseSerializer(serializers.Serializer):
    detail = serializers.CharField()


class ValidationErrorResponseSerializer(serializers.Serializer):
    detail = serializers.CharField(required=False)
    non_field_errors = serializers.ListField(
        child=serializers.CharField(),
        required=False,
    )
    name = serializers.ListField(child=serializers.CharField(), required=False)
    description = serializers.ListField(child=serializers.CharField(), required=False)
    capacity = serializers.ListField(child=serializers.CharField(), required=False)
    price = serializers.ListField(child=serializers.CharField(), required=False)
    is_available = serializers.ListField(
        child=serializers.CharField(),
        required=False,
    )
    room = serializers.ListField(child=serializers.CharField(), required=False)
    hours = serializers.ListField(child=serializers.CharField(), required=False)
    starts_at = serializers.ListField(child=serializers.CharField(), required=False)
    ends_at = serializers.ListField(child=serializers.CharField(), required=False)
    balance = serializers.ListField(child=serializers.CharField(), required=False)
    status = serializers.ListField(child=serializers.CharField(), required=False)
    non_field_errors = serializers.ListField(
        child=serializers.CharField(),
        required=False,
    )
    username = serializers.ListField(child=serializers.CharField(), required=False)
    password = serializers.ListField(child=serializers.CharField(), required=False)
    phone = serializers.ListField(child=serializers.CharField(), required=False)
    ordering = serializers.ListField(child=serializers.CharField(), required=False)
    page = serializers.ListField(child=serializers.CharField(), required=False)
