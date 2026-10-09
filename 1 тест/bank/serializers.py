from rest_framework import serializers

from .models import Book
from .validators import validate_not_blank


class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(trim_whitespace=True, allow_blank=False)
    author = serializers.CharField(trim_whitespace=True, allow_blank=False)

    def validate_title(self, value):
        return validate_not_blank(value, 'Название')

    def validate_author(self, value):
        return validate_not_blank(value, 'Автор')

    class Meta:
        model = Book
        fields = '__all__'