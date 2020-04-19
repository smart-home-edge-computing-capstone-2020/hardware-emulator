from django.db import models

# Create your models here.
class Hardware(models.Model):
    FUNCTION_TYPES = (
        ('S', 'Sensor'),
        ('A', 'Actuator')
    )
    VALUE_TYPES = (
        ('I', 'Integer'),
        ('B', 'Boolean'),
        ('F', 'Float')
    )

    deviceName = models.CharField(max_length=50)
    hardwareName = models.CharField(max_length=50)
    function_type = models.CharField(max_length=1, choices=FUNCTION_TYPES)
    pin = models.IntegerField(default=-1)
    valueType = models.CharField(max_length=10)
    valueInteger = models.IntegerField(default=-1)
    valueBoolean = models.BooleanField(default=False)
    valueFloat = models.FloatField(default=-0.1)

    def __str__(self):
        return self.hardwareName + " function of " + self.deviceName + " device"