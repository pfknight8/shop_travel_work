from django.shortcuts import render
from rest_framework import generics
from shop_travel_work.serializers import LocalFareSerializer, LocationSerializer
from .models import Location, LocalFare

# Create your views here.
class LocationList(generics.ListCreateAPIView):
  queryset = Location.objects.all()
  serializer_class = LocationSerializer

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Location.objects.all()
  serializer_class = LocationSerializer

class LocalFareList(generics.ListCreateAPIView):
  queryset = LocalFare.objects.all()
  serializer_class = LocalFareSerializer

class LocalFareDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = LocalFare.objects.all()
  serializer_class = LocalFareSerializer