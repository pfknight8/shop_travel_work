from django.db import models

# Create your models here.
class Location(models.Model):
  name = models.CharField(max_length=100)
  country = models.CharField(max_length=75)
  state_province = models.CharField(max_length=100)
  city = models.CharField(max_length=100)

  
  def __str__(self):
    return self.name

class LocalFare(models.Model):
  class RateOptions(models.IntegerChoices):
    stay_away = -2
    at_your_risk = -1
    neutral = 0
    recommend = 1
    highly_recommend = 2
  recommend = models.IntegerField(choices=RateOptions.choices)
  name = models.CharField(max_length=100)
  category = models.CharField(max_length=50)
  description = models.TextField()
  establishment = models.CharField(max_length=100)

  def __str__(self):
    return self.name