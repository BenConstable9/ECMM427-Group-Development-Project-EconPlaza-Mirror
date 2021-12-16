from rest_framework import serializers

from ..models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "url", "username", "email", "verified", "is_staff", "first_name", "last_name", "date_joined"]