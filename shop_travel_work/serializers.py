from dataclasses import field
from rest_framework import serializers
from .models import Location, LocalFare, LocalItem, LocationPost
from accounts.models import User

class LocationSerializer(serializers.ModelSerializer):
  localfares = serializers.PrimaryKeyRelatedField(
    many=True,
    read_only=True
  )
  localitems = serializers.PrimaryKeyRelatedField(
    many=True,
    read_only=True
  )
  locationposts = serializers.PrimaryKeyRelatedField(
    many=True,
    read_only=True
  )
  class Meta:
    model = Location
    fields = '__all__'

class LocalFareSerializer(serializers.ModelSerializer):
  location = serializers.StringRelatedField(read_only=True)
  user = serializers.StringRelatedField(read_only=True)
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
  location = serializers.StringRelatedField(read_only=True)
  user = serializers.StringRelatedField(read_only=True)
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
  location = serializers.StringRelatedField(read_only=True)
  user = serializers.StringRelatedField(read_only=True)
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
