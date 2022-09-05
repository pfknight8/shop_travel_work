from django.shortcuts import render
from rest_framework import generics
from shop_travel_work.serializers import LocalFareSerializer, LocationSerializer, LocalItemSerializer, LocationPostSerializer, UserSerializer
from .models import Location, LocalFare, LocalItem, LocationPost, User

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

class LocalItemList(generics.ListCreateAPIView):
  queryset = LocalItem.objects.all()
  serializer_class = LocalItemSerializer

class LocalItemDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = LocalItem.objects.all()
  serializer_class = LocalItemSerializer

class LocationPostList(generics.ListCreateAPIView):
  queryset = LocationPost.objects.all()
  serializer_class = LocationPostSerializer

class LocationPostDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = LocationPost.objects.all()
  serializer_class = LocationPostSerializer

class UserList(generics.ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer