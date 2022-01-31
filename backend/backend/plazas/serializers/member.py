from rest_framework import serializers
from ..models import Member
from accounts.serializers import UserSerializer


class MemberSerializer(serializers.ModelSerializer):
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

        # This ensures the profile is only serialised on a GET not a POST
        representation["user"] = UserSerializer(instance.user).data
        return representation
