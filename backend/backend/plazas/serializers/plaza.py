from rest_framework import serializers
from rest_framework.exceptions import APIException
from ..models import Plaza, Member, Post, Tag
from ..serializers import TagSerializer
import json

from django.core.exceptions import ObjectDoesNotExist


class PlazaSerializer(serializers.HyperlinkedModelSerializer):
    permissions = serializers.JSONField()
    stats = serializers.SerializerMethodField("get_plaza_stats")
    membership = serializers.SerializerMethodField("get_plaza_membership")

    tags = TagSerializer(many=True)

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

    def create(self, validated_data):
        # Allow writeable tags
        # https://www.django-rest-framework.org/api-guide/relations/#writable-nested-serializers

        tags_data = validated_data.pop("tags")
        plaza = Plaza.objects.create(**validated_data)

        # Create a membership against this plaza with the owner type
        Member.objects.create(
            user=self.context["request"].user,
            plaza=plaza,
            member_type="OP",
        )

        for tag_data in tags_data:
            Tag.objects.create(content_object=plaza, tag=tag_data)

        return plaza

    def get_plaza_stats(self, instance):
        return {
            "members": Member.objects.all().filter(plaza=instance).count(),
            "posts": Post.objects.all().filter(plaza=instance).count(),
        }

    def get_plaza_membership(self, instance):
        request = self.context.get("request", None)

        # Must check user is authenticated to avoid error on the member check
        if request is not None and request.user.is_authenticated:
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
        else:
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
