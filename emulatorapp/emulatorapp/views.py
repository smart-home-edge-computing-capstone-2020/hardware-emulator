from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from emulatorapp.models import Hardware
from emulatorapp.serializers import HardwareSerializer

# Create your views here.
def index(request):
    return HttpResponse("Hello world. You're in the emulator")

@api_view(['POST'])
def createHardware(request):
    print(request.data)
    # serializer = DeviceSerializer(data=request.data)
    # if serializer.is_valid():
    #     serializer.save();
    #     return Response(serializer.data, status=status.HTTP_201_CREATE)
    # return Response(serializer.errors, status=status.HTTP_400_REQUEST)
