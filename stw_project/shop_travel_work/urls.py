from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
  path('', views.LocationList.as_view(), name='location_list'),
  path('locations/<int:pk>', views.LocationDetail.as_view(), name='location_detail'),
  path('localfare', views.LocalFareList.as_view(), name='local_fare_list'),
  path('localfare/<int:pk>', views.LocalFareDetail.as_view(), name='local_fare_detail')
]