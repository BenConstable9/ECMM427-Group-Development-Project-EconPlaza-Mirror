from rest_framework import serializers
from rest_framework.exceptions import APIException
import json

from accounts.serializers import ProfileSerializer
from ..models import Comment


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    reactions = serializers.JSONField()
    children = RecursiveField(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = [
            "id",
            "parent",
            "children",
            "profile",
            "content",
            "reactions",
            "created_at",
            "hidden",
            "deleted",
        ]
        lookup_field = "id"

    def to_representation(self, instance):
        # Convert Permissions JSON into a dictionary to be combined into the JSON response
        representation = super(CommentSerializer, self).to_representation(instance)

        try:
            representation["reactions"] = json.loads(representation["reactions"])
        except ValueError as e:
            # Permissions are not valid JSON.
            # Something's wrong here return a 500
            raise APIException("Reactions are formatted incorrectly.", 500)

        # This ensures the profile is only serialised on a GET not a POST
        representation["profile"] = ProfileSerializer(instance.profile).data
        return representation
