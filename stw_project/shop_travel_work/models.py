from django.db import models
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL

# Create your models here.
# class User(models.Model):
#   username = models.CharField(max_length=50, unique=True)
#   first_name = models.CharField(max_length=50)
#   last_name = models.CharField(max_length=50)
#   email = models.EmailField()
#   password_digest = models.CharField(max_length=25)

#   def __str__(self):
#     return self.username

class Location(models.Model):
  name = models.CharField(max_length=100, unique=True)
  country = models.CharField(max_length=75)
  state_province = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class LocalFare(models.Model):
  class RateOptions(models.IntegerChoices):
    stay_away = -1
    neutral = 0
    recommend = 1
  recommend = models.IntegerField(choices=RateOptions.choices, default=0)
  name = models.CharField(max_length=100)
  category = models.CharField(max_length=50)
  description = models.TextField()
  establishment = models.CharField(max_length=100)
  location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='localfares')
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='localfares')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class LocalItem(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  store = models.CharField(max_length=100)
  store_url = models.CharField(max_length=200, null=True, blank=True)
  image = models.CharField(max_length=200)
  location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='localitems')
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='localitems')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class LocationPost(models.Model):
  title = models.CharField(max_length=50)
  body = models.TextField()
  location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='locationposts')
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='locationposts')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title