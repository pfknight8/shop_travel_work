from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from .custompermissions import IsUserAndAuthenticated
from accounts import serializers

# Create your views here.
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
  permission_classes_by_action = {'retrieve': [IsAuthenticated], 'update': [IsUserAndAuthenticated], 'destroy': [IsUserAndAuthenticated | IsAdminUser]}

  # def retrieve(self, request, *args, **kwargs):
  #   return super(UserDetailViewSet, self).retrieve(request, *args, **kwargs)

  def retrieve(self, request, username):
    queryset = User.objects.all()
    user = get_object_or_404(queryset, username=username)
    serializer = UserSerializer(user)
    return Response(serializer.data)
  
  def update(self, request, *args, **kwargs):
    return super(UserDetailViewSet, self).update(request, *args, **kwargs)

  # def destroy(self, request, *args, **kwargs):
  #   return super(UserDetailViewSet, self).destroy(request, *args, **kwargs)

  def destroy(self, request, *args, **kwargs):
    user = self.get_object()
    user.active = False
    user.save()
    response = HttpResponse("User Deleted")
    return response

  def get_permissions(self):
        try:
            # return permission_classes depending on `action` 
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError: 
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]

class CreateUserView(generics.CreateAPIView):
  model = User
  permission_classes = [AllowAny]
  serializer_class = UserSerializer