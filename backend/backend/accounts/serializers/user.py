from rest_framework import serializers, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password

from django.core.exceptions import ValidationError
from rest_framework.exceptions import ValidationError as DRFValidationError
from utils.recaptcha import is_recaptcha_valid



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
            "institutional_affiliation",
            "password",
        ]
        extra_kwargs = {
            "password": {"write_only": True, "required": False},
        }

    def create(self, validated_data):
        print(self.context)
        request = self.context.get('request', None)
        if is_recaptcha_valid(request):
            try:
                password = validated_data.get("password")
                validate_password(validated_data["password"])
                validated_data["password"] = make_password(password)
            except ValidationError as e:
                raise DRFValidationError(e.messages)
            except KeyError as e:
                raise DRFValidationError(detail="Bad Password.")
            return super().create(validated_data)
        else:
            raise DRFValidationError(detail="Recaptcha Failed.")
