from rest_framework import serializers
from ..models import Vouch

#class VouchSerializer(serializers.HyperlinkedModelSerializer):
# TODO: This should be changed to Hyperlinked once the user model is defined
class VouchSerializer(serializers.ModelSerializer):
    voucher = serializers.ReadOnlyField(source='voucher.id')

    class Meta:
        model = Vouch
        fields = ["voucher", "vouchee"]
