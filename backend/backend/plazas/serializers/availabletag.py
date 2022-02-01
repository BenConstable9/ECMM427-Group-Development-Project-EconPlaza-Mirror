from rest_framework import serializers
from ..models import Tag


class AvailableTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            "name",
            "created_at",
        ]

        lookup_field = "id"
