from rest_framework import serializers
from .models import User
from shop_travel_work.serializers import LocalFareSerializer, LocalItemSerializer, LocationPostSerializer
# from shop_travel_work.models import LocalFare, LocalItem, LocationPost

class UserSerializer(serializers.ModelSerializer):

  localfares = LocalFareSerializer(many=True, read_only=True)
  localitems = LocalItemSerializer(many=True, read_only=True)
  locationposts = LocationPostSerializer(many=True, read_only=True)

  class Meta:
    model = User
    fields = '__all__'
    extra_kwargs = {"password": {"write_only": True}}

  def create(self, validated_data):
    user = User.objects.create_user(
      username=validated_data['username'],
      email=validated_data['email'],
      password=validated_data['password'],
      first_name=validated_data['first_name'],
      last_name=validated_data['last_name']
    )
    return user

  def update(self, user, validated_data):
    return user