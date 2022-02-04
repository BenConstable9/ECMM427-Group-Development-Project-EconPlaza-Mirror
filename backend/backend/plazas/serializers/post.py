from rest_framework import serializers
from rest_framework.exceptions import APIException
from django.core.exceptions import ObjectDoesNotExist
from ..models import Post
import json

from accounts.serializers import ProfileSerializer
from ..models import Comment
from ..serializers import TagSerializer


class PostSerializer(serializers.ModelSerializer):
    permissions = serializers.JSONField()
    reactions = serializers.JSONField()
    replies = serializers.SerializerMethodField("get_comments_count")
    last_activity = serializers.SerializerMethodField()

    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "profile",
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

    def get_comments_count(self, instance):
        return Comment.objects.filter(post=instance).count()

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
