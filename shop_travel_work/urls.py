from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
  path('locations', views.LocationListView.as_view({'get': 'list', 'post': 'create'}), name='location-list'),
  path('locations/<int:pk>', views.LocationDetailSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='location-detail'),
  # Local Fare paths
  path('localfare', views.LocalFareList.as_view()),
  path('localfare', views.LocalFareCreateList.as_view(), name='localfare-list'),
  path('localfare/<int:pk>', views.LocalFareDetailSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='localfare-detail'),
  # path('localfare/<int:location_id', views.LocalFaresByLocation, name='localfare-location'),
  # Local Item paths
  path('localitem', views.LocalItemList.as_view()),
  path('localitem', views.LocalItemCreateList.as_view(), name='localitem-list'),
  path('localitems/<int:pk>', views.LocalItemDetailSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='localitem-detail'),
  # Location Blog Post paths
  path('locations/posts', views.LocationPostListView.as_view()),
  path('locations/posts', views.LocationPostCreateListView.as_view({'get': 'list', 'post': 'create'}), name='locationpost-list'),
  path('locations/posts/<int:pk>', views.LocationPostDetailSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='locationpost-detail'),
]