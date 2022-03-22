from django.shortcuts import render

from methodBased.models import Buildings
from methodBased.serializers import BuildingsModalSerializer
from rest_framework import generics


class building_list(generics.ListCreateAPIView):
    queryset = Buildings.objects.all()
    serializer_class = BuildingsModalSerializer


class building_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Buildings.objects.all()
    serializer_class = BuildingsModalSerializer

