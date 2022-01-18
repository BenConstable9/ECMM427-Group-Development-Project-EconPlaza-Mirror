from rest_framework import serializers
from rest_framework.exceptions import APIException
from ..models import Plaza, Member, Post
import json


class PlazaSerializer(serializers.HyperlinkedModelSerializer):
    permissions = serializers.JSONField()
    stats = serializers.SerializerMethodField("get_plaza_stats")

    class Meta:
        model = Plaza
        fields = [
            "id",
            "slug",
            "name",
            "description",
            "created_at",
            "permissions",
            "stats",
        ]
        lookup_field = "slug"

    def get_plaza_stats(self, instance):
        return {
            "members": Member.objects.all().filter(plaza=instance).count(),
            "posts": Post.objects.all().filter(plaza=instance).count(),
        }

    def to_representation(self, instance):
        # Convert Permissions JSON into a dictionary to be combined into the JSON response
        representation = super(PlazaSerializer, self).to_representation(instance)
        try:
            representation["permissions"] = json.loads(representation["permissions"])
        except ValueError as e:
            # Permissions are not valid JSON.
            # Something's wrong here return a 500
            raise APIException("Permissions are formatted incorrectly.", 500)
        return representation
