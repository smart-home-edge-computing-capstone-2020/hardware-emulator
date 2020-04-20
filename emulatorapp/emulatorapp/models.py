from django.db import models

# Create your models here.
class Hardware(models.Model):
    FUNCTION_TYPES = (
        ('s', 'Sensor'),
        ('a', 'Actuator'),
        ('n', 'Not Set')
    )
    VALUE_TYPES = (
        ('i', 'Integer'),
        ('b', 'Boolean'),
        ('f', 'Float'),
        ('n', 'Not Set')
    )

    deviceName = models.CharField(max_length=50)
    hardwareName = models.CharField(max_length=50)
    hardwareType = models.CharField(max_length=1, choices=FUNCTION_TYPES, default='n')
    pin = models.IntegerField(default=-1)
    valueType = models.CharField(max_length=1, choices=VALUE_TYPES, default='n')
    valueInteger = models.IntegerField(default=-1)
    valueBoolean = models.BooleanField(default=False)
    valueFloat = models.FloatField(default=-0.1)

    def __str__(self):
        return self.hardwareName + " function of " + self.deviceName + " device"