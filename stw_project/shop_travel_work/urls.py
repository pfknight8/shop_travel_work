from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
  path('', views.LocationList.as_view(), name='location-list'),
  path('locations/<int:pk>', views.LocationDetail.as_view(), name='location-detail'),
  path('localfare', views.LocalFareList.as_view(), name='localfare-list'),
  path('localfare/<int:pk>', views.LocalFareDetail.as_view(), name='localfare-detail'),
  path('localitem', views.LocalItemList.as_view(), name='localitem-list'),
  path('localitem/<int:pk>', views.LocalItemDetail.as_view(), name='localitem-detail'),
  path('locations/posts', views.LocationPostList.as_view(), name='locationpost-list'),
  path('locations/posts/<int:pk>', views.LocationPostDetail.as_view(), name='locationpost-detail'),
  #editing these to make them have auth.
  path('users', views.UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
  path('users/<int:pk>', views.UserDetailViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user-detail'),
  path('obtain', obtain_auth_token)
]