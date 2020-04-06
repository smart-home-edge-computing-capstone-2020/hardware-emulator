from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from emulatorapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('devices/', views.device_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)