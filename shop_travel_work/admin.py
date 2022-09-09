from django.contrib import admin
from .models import Location, LocalFare, LocalItem, LocationPost
# Register your models here.
admin.site.register(Location)
admin.site.register(LocalFare)
admin.site.register(LocalItem)
admin.site.register(LocationPost)