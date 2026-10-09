from rest_framework import serializers
from .models import Task
class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=('id','title','description','is_complete')
        read_only_fields=('id',)
    def validate_title(self,value):
        if not value or not value.strip():
            raise serializers.ValidationError("Поле тайтл не может быть пустым")
        if len(value.strip())<3:
            raise serializers.ValidationError("Поле тайтл должен иметь не менее 3 символов")
        return value.strip()
    