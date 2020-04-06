from .models import Device, Function
from rest_framework import serializers


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['name', 'description']

class FunctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Function
        fields = ['device', 'name', 'description', 'function_type']