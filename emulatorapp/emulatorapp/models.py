from django.db import models

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Function(models.Model):
    FUNCTION_TYPES = (
        ('S', 'Sensor'),
        ('A', 'Actuator')
    )

    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    function_type = models.CharField(max_length=1, choices=FUNCTION_TYPES)

    def __str__(self):
        return self.name + " function of " + self.device + " device"