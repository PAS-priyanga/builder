from django.contrib import admin

# Register your models here.

# import your models here
from .models import Builder,PropertyDetails
# Register your models here
admin.site.register(Builder)

admin.site.register(PropertyDetails)