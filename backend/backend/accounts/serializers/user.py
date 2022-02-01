from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "username",
            "email",
            "verified",
            "is_staff",
            "first_name",
            "last_name",
            "date_joined",
        ]

class UserPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        read_only_fields = ["id"]
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
        ]
        extra_kwargs = {
            "password": {"write_only": True, "required": False},
        }
