from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from emulatorapp.models import Device
from emulatorapp.serializers import DeviceSerializer

# Create your views here.
def index(request):
    return HttpResponse("Hello world. You're in the emulator")

@api_view(['GET', 'POST'])
def device_list(request):
    if request.method == 'GET':
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATE)
        return Response(serializer.errors, status=status.HTTP_400_REQUEST)
