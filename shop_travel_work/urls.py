from django.urls import path
from . import views


urlpatterns = [
  path('locations', views.LocationListView.as_view({'get': 'list', 'post': 'create'}), name='location-list'),
  path('locations/<int:pk>', views.LocationDetailSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='location-detail'),
  # Local Fare paths
  path('localfare/view', views.LocalFareList.as_view()),
  path('localfare', views.LocalFareCreateList.as_view(), name='localfare-list'),
  path('localfare/<int:pk>', views.LocalFareDetailSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='localfare-detail'),
  # Local Item paths
  path('localitem/view', views.LocalItemList.as_view()),
  path('localitems', views.LocalItemCreateList.as_view(), name='localitem-list'),
  path('localitems/<int:pk>', views.LocalItemDetailSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='localitem-detail'),
  # Location Blog Post paths
  path('locations/post/view', views.LocationPostListView.as_view()),
  path('locations/posts', views.LocationPostCreateListView.as_view({'get': 'list', 'post': 'create'}), name='locationpost-list'),
  path('locations/posts/<int:pk>', views.LocationPostDetailSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='locationpost-detail'),
]