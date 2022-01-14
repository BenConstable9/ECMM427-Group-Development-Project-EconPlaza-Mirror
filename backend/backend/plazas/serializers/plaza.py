from rest_framework import serializers
from rest_framework.exceptions import APIException
from ..models import Plaza
import json

class PlazaSerializer(serializers.HyperlinkedModelSerializer):

    permissions = serializers.JSONField()

    class Meta:
        model = Plaza
        fields = ["id", "slug", "name", "description",
                  "created_at", "permissions"]

    def to_representation(self, instance):
        # Convert Permissions JSON into a dictionary to be combined into the JSON response
        representation = super(PlazaSerializer, self).to_representation(instance)
        try:
            representation['permissions'] = json.loads(representation['permissions'])
        except ValueError as e:
            # Permissions are not valid JSON.
            # Something's wrong here return a 500
            raise APIException('Permissions are formatted incorrectly.', 500)
        return representation