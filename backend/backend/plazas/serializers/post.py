from rest_framework import serializers
from rest_framework.exceptions import APIException
from django.core.exceptions import ObjectDoesNotExist

from ..models import Post
import json

from accounts.serializers import ProfileSerializer
from ..models import Comment, Post, Tag, AvailableTag
from ..serializers import TagSerializer, PlazaSerializer


class PostSerializer(serializers.ModelSerializer):
    permissions = serializers.JSONField()
    reactions = serializers.JSONField()

    replies = serializers.IntegerField(read_only=True)
    last_activity = serializers.DateTimeField(read_only=True)

    tags = TagSerializer(many=True)
    plaza = PlazaSerializer(many=False, read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "profile",
            "plaza",
            "title",
            "content",
            "permissions",
            "reactions",
            "hidden",
            "views",
            "replies",
            "last_activity",
            "created_at",
            "tags",
        ]
        lookup_field = "id"

    def create(self, validated_data):
        # Allow writeable tags
        # https://www.django-rest-framework.org/api-guide/relations/#writable-nested-serializers

        tags_data = validated_data.pop("tags")
        post = Post.objects.create(**validated_data)

        for tag_data in tags_data:
            Tag.objects.create(content_object=post, tag=tag_data)

        return post

    def get_last_activity(self, instance):
        # Get the last comment on the post

        try:
            last_comment = Comment.objects.filter(post=instance).latest("created_at")

            return last_comment.created_at
        except ObjectDoesNotExist:

            return instance.created_at

    def to_representation(self, instance):
        # Convert Permissions JSON into a dictionary to be combined into the JSON response
        representation = super().to_representation(instance)

        try:
            representation["permissions"] = json.loads(representation["permissions"])
        except ValueError as e:
            # Permissions are not valid JSON.
            # Something's wrong here return a 500
            raise APIException("Permissions are formatted incorrectly.", 500)
        try:
            representation["reactions"] = json.loads(representation["reactions"])
        except ValueError as e:
            # Permissions are not valid JSON.
            # Something's wrong here return a 500
            raise APIException("Reactions are formatted incorrectly.", 500)

        # This ensures the profile is only serialised on a GET not a POST
        representation["profile"] = ProfileSerializer(instance.profile).data

        return representation
