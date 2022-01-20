from rest_framework import serializers
from rest_framework.exceptions import APIException
from ..models import Post
import json

from accounts.serializers import ProfileSerializer
from ..models import Comment


class PostSerializer(serializers.ModelSerializer):
    permissions = serializers.JSONField()
    reactions = serializers.JSONField()
    profile = ProfileSerializer()
    replies = serializers.SerializerMethodField("count_comments")

    class Meta:
        model = Post
        fields = [
            "id",
            "profile",
            "title",
            "content",
            "permissions",
            "reactions",
            "views",
            "replies",
            "created_at",
        ]
        lookup_field = "slug"

    def count_comments(self, instance):
        return Comment.objects.all().filter(post=instance).count()

    def to_representation(self, instance):
        # Convert Permissions JSON into a dictionary to be combined into the JSON response
        representation = super(PostSerializer, self).to_representation(instance)
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
        return representation
