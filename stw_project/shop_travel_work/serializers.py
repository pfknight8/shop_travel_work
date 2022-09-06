from dataclasses import field
from rest_framework import serializers
from .models import Location, LocalFare, LocalItem, LocationPost
from accounts.serializers import UserSerializer
from accounts.models import User

class LocationSerializer(serializers.ModelSerializer):
  localfares = serializers.HyperlinkedRelatedField(
    view_name='localfare-detail',
    many=True,
    read_only=True
  )
  localitems = serializers.HyperlinkedRelatedField(
    view_name='localitem-detail',
    many=True,
    read_only=True
  )
  locationposts = serializers.HyperlinkedRelatedField(
    view_name='locationpost-detail',
    many=True,
    read_only=True
  )
  class Meta:
    model = Location
    fields = ['id', 'name', 'country', 'state_province', 'city', 'localfares', 'localitems', 'locationposts']

# class UserSerializer(serializers.ModelSerializer):
#   localfares = serializers.HyperlinkedRelatedField(
#     view_name='localfare-detail',
#     many=True,
#     read_only=True
#   )
#   localitems = serializers.HyperlinkedRelatedField(
#     view_name='localitem-detail',
#     many=True,
#     read_only=True
#   )
#   locationposts = serializers.HyperlinkedRelatedField(
#     view_name='locationpost-detail',
#     many=True,
#     read_only=True
#   )
#   class Meta:
#     model = User
#     fields = '__all__'

class LocalFareSerializer(serializers.ModelSerializer):
  location = serializers.HyperlinkedRelatedField(
    view_name='location-detail',
    read_only=True
  )
  # user = serializers.HyperlinkedRelatedField(
  #   view_name='user-detail',
  #   read_only=True
  # )
  user = UserSerializer(view_name='user-detail', read_only=True)
  location_id = serializers.PrimaryKeyRelatedField(
    queryset=Location.objects.all(),
    source='location'
  )
  user_id = serializers.PrimaryKeyRelatedField(
    queryset=User.objects.all(),
    source='user'
  )
  class Meta:
    model = LocalFare
    fields = '__all__'

class LocalItemSerializer(serializers.ModelSerializer):
  location = serializers.HyperlinkedRelatedField(
    view_name='location-detail',
    read_only=True
  )
  user = serializers.HyperlinkedRelatedField(
    view_name='user-detail',
    read_only=True
  )
  location_id = serializers.PrimaryKeyRelatedField(
    queryset=Location.objects.all(),
    source='location'
  )
  user_id = serializers.PrimaryKeyRelatedField(
    queryset=User.objects.all(),
    source='user'
  )
  class Meta:
    model = LocalItem
    fields = '__all__'

class LocationPostSerializer(serializers.ModelSerializer):
  location = serializers.HyperlinkedRelatedField(
    view_name='location-detail',
    read_only=True
  )
  user = serializers.HyperlinkedRelatedField(
    view_name='user-detail',
    read_only=True
  )
  location_id = serializers.PrimaryKeyRelatedField(
    queryset=Location.objects.all(),
    source='location'
  )
  user_id = serializers.PrimaryKeyRelatedField(
    queryset=User.objects.all(),
    source='user'
  )
  class Meta:
    model = LocationPost
    fields = '__all__'
