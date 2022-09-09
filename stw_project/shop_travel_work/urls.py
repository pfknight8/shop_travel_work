from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
  path('locations', views.LocationListView.as_view({'get': 'list', 'post': 'create'}), name='location-list'),
  path('locations/<int:pk>', views.LocationDetailSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='location-detail'),
  # Local Fare paths
  path('localfare', views.LocalFareList.as_view(), name='localfare-list'),
  path('localfare/<int:pk>', views.LocalFareDetailSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='localfare-detail'),
  # Local Item paths
  path('localitems', views.LocalItemList.as_view(), name='localitem-list'),
  path('localitems/<int:pk>', views.LocalItemDetailSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='localitem-detail'),
  # Location Blog Post paths
  path('locations/posts', views.LocationPostListView.as_view({'get': 'list', 'post': 'create'}), name='locationpost-list'),
  path('locations/posts/<int:pk>', views.LocationPostDetailSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='locationpost-detail'),
]