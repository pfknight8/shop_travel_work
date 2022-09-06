from django.contrib import admin
from .models import Location, LocalFare, LocalItem, LocationPost, User
# Register your models here.
admin.site.register(Location)
admin.site.register(LocalFare)
admin.site.register(LocalItem)
admin.site.register(LocationPost)
admin.site.register(User)