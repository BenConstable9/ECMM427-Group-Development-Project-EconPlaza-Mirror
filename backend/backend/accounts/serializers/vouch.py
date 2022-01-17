from rest_framework import serializers
from ..models import Vouch
from ..serializers import UserSerializer


class VouchSerializer(serializers.ModelSerializer):
    voucher = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Vouch
        fields = ["voucher", "vouchee"]
