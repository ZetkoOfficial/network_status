from django.contrib import admin
from .models import Service, Website

admin.site.register(Website)
admin.site.register(Service)