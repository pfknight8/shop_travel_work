from rest_framework import serializers
from .models import Location, LocalFare

class LocationSerializer(serializers.ModelSerializer):
  # localfares = serializers.HyperlinkedRelatedField(
  #   view_name='local_fare_detail',
  #   many=True,
  #   read_only=True
  # )
  class Meta:
    model = Location
    fields = '__all__'

class LocalFareSerializer(serializers.ModelSerializer):
  location = serializers.HyperlinkedRelatedField(
    view_name='location_detail',
    read_only=True
  )
  class Meta:
    model = LocalFare
    fields = '__all__'
