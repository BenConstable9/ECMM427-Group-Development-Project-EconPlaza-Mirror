from rest_framework import serializers
from rest_framework.exceptions import APIException
from ..models import Plaza, Member, Post
from ..serializers import TagSerializer
import json

from django.core.exceptions import ObjectDoesNotExist


class TagObjectRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        """
        Serialize tagged objects to a simple textual representation.
        """
        print(value.get_queryset())
        # print(value.get_queryset()[0])

        for query in value.get_queryset():
            print(TagSerializer(query))

        serializer = TagSerializer(value.get_queryset())

        return serializer.data


class PlazaSerializer(serializers.HyperlinkedModelSerializer):
    permissions = serializers.JSONField()
    stats = serializers.SerializerMethodField("get_plaza_stats")
    membership = serializers.SerializerMethodField("get_plaza_membership")

    tags = TagObjectRelatedField(read_only=True)

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
            "membership",
            "tags",
        ]
        lookup_field = "slug"

    def get_plaza_stats(self, instance):
        return {
            "members": Member.objects.all().filter(plaza=instance).count(),
            "posts": Post.objects.all().filter(plaza=instance).count(),
        }

    def get_plaza_membership(self, instance):
        request = self.context.get("request", None)

        try:
            return {
                "member": True,
                "type": Member.objects.get(
                    plaza=instance, user=request.user
                ).member_type,
            }
        except ObjectDoesNotExist:
            return {
                "member": False,
                "type": None,
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
