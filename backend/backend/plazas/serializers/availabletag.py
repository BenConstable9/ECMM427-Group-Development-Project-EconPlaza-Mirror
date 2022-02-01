from rest_framework import serializers
from ..models import AvailableTag


class AvailableTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableTag
        fields = [
            "id",
            "name",
            "created_at",
        ]

        lookup_field = "id"
