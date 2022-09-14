from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from .custompermissions import IsOwnerAndAuthenticated
from shop_travel_work.serializers import LocalFareSerializer, LocationSerializer, LocalItemSerializer, LocationPostSerializer
from .models import Location, LocalFare, LocalItem, LocationPost

###########################
## - Location Listings - ##
###########################

class LocationListView(viewsets.ModelViewSet):
  queryset = Location.objects.all()
  serializer_class = LocationSerializer
  permission_classes_by_action = {'list': [AllowAny], 'create': [IsAdminUser]}
  authentication_classes = ()

  def list(self, request, *args, **kwargs):
    return super(LocationListView, self).list(request, *args, **kwargs)

  def create(self, request, *args, **kwargs):
    return super(LocationListView, self).create(request, *args, **kwargs)

  def get_permissions(self):
        try:
            # return permission_classes depending on `action` 
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError: 
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]

class LocationDetailSet(viewsets.ModelViewSet):
  queryset = Location.objects.all()
  serializer_class = LocationSerializer
  permission_classes_by_action = {'retrieve': [AllowAny], 'update': [IsAdminUser], 'destroy': [IsAdminUser]}
  
  def retrieve(self, request, *args, **kwargs):
    return super(LocationDetailSet, self).retrieve(request, *args, **kwargs)
  
  def update(self, request, *args, **kwargs):
    return super(LocationDetailSet, self).update(request, *args, **kwargs)

  def destroy(self, request, *args, **kwargs):
    return super(LocationDetailSet, self).destroy(request, *args, **kwargs)

  def get_permissions(self):
        try:
            # return permission_classes depending on `action` 
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError: 
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]

##########################
## - Local Fare Posts - ##
##########################

class LocalFareList(generics.ListAPIView):
  serializer_class = LocalFareSerializer
  permission_classes = [AllowAny]

  def get_queryset(self):
    id = self.request.GET.get('id','')
    if id:
      id = int(id)
    else:
      id = 0
    return LocalFare.objects.filter(location=id)

class LocalFareCreateList(generics.ListCreateAPIView):
  queryset = LocalFare.objects.all()
  serializer_class = LocalFareSerializer

class LocalFareDetailSet(viewsets.ModelViewSet):
  queryset = LocalFare.objects.all()
  serializer_class = LocalFareSerializer
  permission_classes_by_action = {'retrieve': [IsAuthenticated], 'update': [IsOwnerAndAuthenticated], 'destroy': [IsOwnerAndAuthenticated]}

  def retrieve(self, request, *args, **kwargs):
    return super(LocalFareDetailSet, self).retrieve(request, *args, **kwargs)
  
  def update(self, request, *args, **kwargs):
    return super(LocalFareDetailSet, self).update(request, *args, **kwargs)

  def destroy(self, request, *args, **kwargs):
    return super(LocalFareDetailSet, self).destroy(request, *args, **kwargs)

  def get_permissions(self):
        try:
            # return permission_classes depending on `action` 
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError: 
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]

##########################
## - local Item Posts - ##
##########################

class LocalItemList(generics.ListCreateAPIView):
  serializer_class = LocalItemSerializer
  permission_classes = [AllowAny]
  def get_queryset(self):
    id = self.request.GET.get('id','')
    if id:
      id = int(id)
    else:
      id = 0
    return LocalItem.objects.filter(location=id)

class LocalItemCreateList(generics.ListCreateAPIView):
  queryset = LocalItem.objects.all()
  serializer_class = LocalItemSerializer
  permission_classes_by_action = {'list': [AllowAny], 'create': [IsAuthenticated]}

class LocalItemDetailSet(viewsets.ModelViewSet):
  queryset = LocalItem.objects.all()
  serializer_class = LocalItemSerializer
  permission_classes_by_action = {'retrieve': [IsAuthenticated], 'update': [IsOwnerAndAuthenticated], 'destroy': [IsOwnerAndAuthenticated]}

  def retrieve(self, request, *args, **kwargs):
    return super(LocalItemDetailSet, self).retrieve(request, *args, **kwargs)
  
  def update(self, request, *args, **kwargs):
    return super(LocalItemDetailSet, self).update(request, *args, **kwargs)

  def destroy(self, request, *args, **kwargs):
    return super(LocalItemDetailSet, self).destroy(request, *args, **kwargs)

  def get_permissions(self):
        try:
            # return permission_classes depending on `action` 
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError: 
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]

########################
## - Location Posts - ##
########################

class LocationPostListView(generics.ListAPIView):
  serializer_class = LocationPostSerializer
  permission_classes = [AllowAny]

  def get_queryset(self):
    id = self.request.GET.get('id','')
    if id:
      id = int(id)
    else:
      id = 0
    return LocationPost.objects.filter(location=id)

class LocationPostCreateListView(viewsets.ModelViewSet):
  queryset = LocationPost.objects.all()
  serializer_class = LocationPostSerializer
  permission_classes_by_action = {'list': [AllowAny], 'create': [IsAuthenticated]}

  def list(self, request, *args, **kwargs):
    return super(LocationPostCreateListView, self).list(request, *args, **kwargs)

  def create(self, request, *args, **kwargs):
    return super(LocationPostCreateListView, self).create(request, *args, **kwargs)

  def get_permissions(self):
        try:
            # return permission_classes depending on `action` 
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError: 
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]

class LocationPostDetailSet(viewsets.ModelViewSet):
  queryset = LocationPost.objects.all()
  serializer_class = LocationPostSerializer
  permission_classes_by_action = {'retrieve': [AllowAny], 'update': [IsOwnerAndAuthenticated], 'destroy': [IsOwnerAndAuthenticated]}

  def retrieve(self, request, *args, **kwargs):
    return super(LocationPostDetailSet, self).retrieve(request, *args, **kwargs)
  
  def update(self, request, *args, **kwargs):
    return super(LocationPostDetailSet, self).update(request, *args, **kwargs)

  def destroy(self, request, *args, **kwargs):
    return super(LocationPostDetailSet, self).destroy(request, *args, **kwargs)

  def get_permissions(self):
        try:
            # return permission_classes depending on `action` 
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError: 
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]
