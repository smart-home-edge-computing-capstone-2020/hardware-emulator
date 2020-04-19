from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
import emulatorapp.views as views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.createHardware),
]

urlpatterns = format_suffix_patterns(urlpatterns)