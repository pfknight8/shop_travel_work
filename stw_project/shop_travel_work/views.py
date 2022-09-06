from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
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

# class UserList(generics.ListCreateAPIView):
#   queryset = User.objects.all()
#   serializer_class = UserSerializer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#   queryset = User.objects.all()
#   serializer_class = UserSerializer

# Altenative views
class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes_by_action = {'create': [AllowAny], 'list': [IsAdminUser]}

  def create(self, request, *args, **kwargs):
    return super(UserViewSet, self).create(request, *args, **kwargs)
  
  def list(self, request, *args, **kwargs):
    return super(UserViewSet, self).list(request, *args, **kwargs)

  def get_permissions(self):
        try:
            # return permission_classes depending on `action` 
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError: 
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]

class UserDetailViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes_by_action = {'retrieve': [IsAuthenticated], 'update': [IsAdminUser], 'destroy': [IsAdminUser]}

  def retrieve(self, request, *args, **kwargs):
    return super(UserDetailViewSet, self).retrieve(request, *args, **kwargs)
  
  def update(self, request, *args, **kwargs):
    return super(UserDetailViewSet, self).update(request, *args, **kwargs)

  def destroy(self, request, *args, **kwargs):
    return super(UserDetailViewSet, self).destroy(request, *args, **kwargs)

  def get_permissions(self):
        try:
            # return permission_classes depending on `action` 
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError: 
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]