from rest_framework import serializers
from ..models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            "id",
            "display_name",
            "global_anonymous",
            "reputation",
            "created_at",
            "user",
        ]

    def get_user(self, instance):
        # Only return the user if the profile is not annoymous
        if instance.global_anonymous:
            return None
        else:
            return instance.user.id
