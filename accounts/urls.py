from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
  path('users', views.UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
  path('users/<str:username>', views.UserDetailViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user-detail'),
  path('obtain', obtain_auth_token),
  path('signup', views.CreateUserView.as_view()),
  # For authentication:
  path('token', TokenObtainPairView.as_view(), name='token-obtain-view'),
  path('token/refresh', TokenRefreshView.as_view(), name='token-refresh'),
  path('token/verify', TokenVerifyView.as_view(), name='token-verify'),
]