from rest_framework import permissions

class IsUserAndAuthenticated(permissions.BasePermission):
  message = "You must be logged in as the owner of this content to modify it."
  def has_permission(self, request, view):
    return request.user and request.user.is_authenticated
  def has_object_permission(self, request, view, obj):
    return obj == request.user