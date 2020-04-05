from django.db import models

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

class Function(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    FUNCTION_TYPES = (
        ('S', 'Sensor'),
        ('A', 'Actuator')
    )
    function_type = models.CharField(max_length=1, choices=FUNCTION_TYPES)