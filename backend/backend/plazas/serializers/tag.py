from rest_framework import serializers

from ..models import Tag
from ..serializers import AvailableTagSerializer


class TagSerializer(serializers.ModelSerializer):
    tag = AvailableTagSerializer(read_only=True)

    class Meta:
        model = Tag
        fields = [
            "id",
            "tag",
            "created_at",
        ]

        lookup_field = "id"
