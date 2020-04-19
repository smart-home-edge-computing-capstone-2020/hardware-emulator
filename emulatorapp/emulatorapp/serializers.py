from .models import Hardware
from rest_framework import serializers

class HardwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hardware
        fields = ['deviceName', 'hardwareName', 'function_type', 'pin', 'valueType', 'valueInteger', 'valueBoolean', 'valueFloat']
