from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from .custompermissions import IsOwnerAndAuthenticated
from shop_travel_work.serializers import LocalFareSerializer, LocationSerializer, LocalItemSerializer, LocationPostSerializer
# from accounts.serializers import UserSerializer
from .models import Location, LocalFare, LocalItem, LocationPost
# from accounts.models import User

###########################
## - Location Listings - ##
###########################

class LocationListView(viewsets.ModelViewSet):
  queryset = Location.objects.all()
  serializer_class = LocationSerializer
  permission_classes_by_action = {'list': [AllowAny], 'create': [IsAdminUser]}

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

class LocalFareList(generics.ListCreateAPIView):
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
  queryset = LocalItem.objects.all()
  serializer_class = LocalItemSerializer

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

class LocationPostListView(viewsets.ModelViewSet):
  queryset = LocationPost.objects.all()
  serializer_class = LocationPostSerializer
  permission_classes_by_action = {'list': [AllowAny], 'create': [IsAuthenticated]}

  def list(self, request, *args, **kwargs):
    return super(LocationPostListView, self).list(request, *args, **kwargs)

  def create(self, request, *args, **kwargs):
    return super(LocationPostListView, self).create(request, *args, **kwargs)

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
  permission_classes_by_action = {'retrieve': [IsAuthenticated], 'update': [IsOwnerAndAuthenticated], 'destroy': [IsOwnerAndAuthenticated]}

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

#######################
## obsolete - moved user stuff to accounts, delete this if works without it here.
#######################

# class UserList(generics.ListCreateAPIView):
#   queryset = User.objects.all()
#   serializer_class = UserSerializer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#   queryset = User.objects.all()
#   serializer_class = UserSerializer

# Altenative views
# class UserViewSet(viewsets.ModelViewSet):
#   queryset = User.objects.all()
#   serializer_class = UserSerializer
#   permission_classes_by_action = {'create': [AllowAny], 'list': [IsAdminUser]}

#   def create(self, request, *args, **kwargs):
#     return super(UserViewSet, self).create(request, *args, **kwargs)
  
#   def list(self, request, *args, **kwargs):
#     return super(UserViewSet, self).list(request, *args, **kwargs)

#   def get_permissions(self):
#         try:
#             # return permission_classes depending on `action` 
#             return [permission() for permission in self.permission_classes_by_action[self.action]]
#         except KeyError: 
#             # action is not set return default permission_classes
#             return [permission() for permission in self.permission_classes]

# class UserDetailViewSet(viewsets.ModelViewSet):
#   queryset = User.objects.all()
#   serializer_class = UserSerializer
#   permission_classes_by_action = {'retrieve': [IsAuthenticated], 'update': [IsAdminUser], 'destroy': [IsAdminUser]}

#   def retrieve(self, request, *args, **kwargs):
#     return super(UserDetailViewSet, self).retrieve(request, *args, **kwargs)
  
#   def update(self, request, *args, **kwargs):
#     return super(UserDetailViewSet, self).update(request, *args, **kwargs)

#   def destroy(self, request, *args, **kwargs):
#     return super(UserDetailViewSet, self).destroy(request, *args, **kwargs)

#   def get_permissions(self):
#         try:
#             # return permission_classes depending on `action` 
#             return [permission() for permission in self.permission_classes_by_action[self.action]]
#         except KeyError: 
#             # action is not set return default permission_classes
#             return [permission() for permission in self.permission_classes]