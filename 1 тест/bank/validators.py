from rest_framework import serializers

def validate_not_blank(value, field_name):
    if value is None or not str(value).strip():
        raise serializers.ValidationError(f'{field_name} не может быть пустым.')
    return value
