from django.urls import path
from . import views
from django.conf import settings as config

urlpatterns = [
    path("", views.index, name="index"),  
]

if config.CONFIG_JSON["allow_manual_search"]:
    urlpatterns.append(path("check_website", views.check_website_view, name="check_website"))