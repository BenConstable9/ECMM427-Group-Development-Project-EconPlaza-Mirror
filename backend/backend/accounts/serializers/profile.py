from rest_framework import serializers
from ..models import Profile


class ProfileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Profile
        fields = ["display_name",
                  "global_anonymous", "reputation", "created_at"]
