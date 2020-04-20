from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
import emulatorapp.views as views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.createHardware),
    path('value/<str:deviceName>/<str:hardwareName>', views.hardwareValue)
]

urlpatterns = format_suffix_patterns(urlpatterns)