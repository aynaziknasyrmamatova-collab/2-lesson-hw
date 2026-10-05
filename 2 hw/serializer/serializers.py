from rest_framework import serializers
from .models import Car
class ModelSerializers(serializers.ModelSerializer):
    class Meta:
        model=Car
        fields=('id','name','description','price')
        read_only_fields=('id',)
    def validate_title(self,value):
        if not value or not value.strip():
            raise serializers.ValidationError("Поле имя не может быть пустым")
        if len(value)<3:
            raise serializers.ValidationError("Поле имя должно иметь не менее 3 символов")
        return value.strip()