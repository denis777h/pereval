from django.urls import path
from rest_framework import serializers
from pereval_data.views import PerevalCreateViewset

urlpatterns = [

    path('submitData/', PerevalCreateViewset.as_view({'get': 'list'}), name='pereval'),




]




