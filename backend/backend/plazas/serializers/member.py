from rest_framework import serializers
from ..models import Member
from accounts.serializers import UserSerializer


class MemberSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Member
        fields = [
            "id",
            "user",
            "member_type",
            "created_at",
        ]

        lookup_field = "user"

    def to_representation(self, instance):
        # Convert Permissions JSON into a dictionary to be combined into the JSON response
        representation = super().to_representation(instance)

        return representation
