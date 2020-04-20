from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from emulatorapp.models import Hardware
from emulatorapp.serializers import HardwareSerializer
from rest_framework.parsers import JSONParser

# Create your views here.
def index(request):
    return HttpResponse("Hello world. You're in the emulator")

@api_view(['POST'])
def createHardware(request):
    serializer = HardwareSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save();
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def hardwareValue(request, deviceName, hardwareName):
    try:
        hardware = Hardware.objects.get(deviceName=deviceName, hardwareName=hardwareName)
    except Hardware.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        response = {'value': 0}

        if 'i' == hardware.valueType:
            response["value"] = hardware.valueInteger

        elif 'b' == hardware.valueType:
            response["value"] = hardware.valueBoolean
        
        else:
            response["value"] = hardware.valueFloat
        
        return Response(data=response, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        data = request.data
        print("Dataval: " + str(data["value"]))

        if 'i' == hardware.valueType:
            hardware.valueInteger = data["value"]

        elif 'b' == hardware["valueType"]:
            hardware.valueBoolean = data["value"]
        
        else:
            hardware.valueFloat = data["value"]
        hardware.save()
        
        return Response(status=status.HTTP_200_OK)