from rest_framework import serializers
from .models import Visitors, Zone


class VisitorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitors
        fields = "__all__"
class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model=Zone
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at")
    visitors_count = serializers.IntegerField(source="visitors.count", read_only=True)