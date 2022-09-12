from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
# if would need to use simplejwt instead:
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
  path('users', views.UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
  path('users/<int:pk>', views.UserDetailViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user-detail'),
  path('obtain', obtain_auth_token),
  path('signup', views.CreateUserView.as_view()),
  # If need to install simple jwt:
  # path('token', TokenObtainPairView.as_view(), name='token-obtain-view'),
  # path('token/refresh', TokenRefreshView.as_view(), name='token-refresh')
]