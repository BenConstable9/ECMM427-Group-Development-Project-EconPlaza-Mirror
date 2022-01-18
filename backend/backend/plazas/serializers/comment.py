from rest_framework import serializers
from rest_framework.exceptions import APIException
import json

from accounts.serializers import ProfileSerializer
from ..models import Comment


class CommentSerializer(serializers.ModelSerializer):
    reactions = serializers.JSONField()
    profile = ProfileSerializer()

    class Meta:
        model = Comment
        fields = [
            "id",
            "profile",
            "content",
            "reactions",
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
        return representation
