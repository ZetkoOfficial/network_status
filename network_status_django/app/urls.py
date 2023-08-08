from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("check_website", views.check_website_view, name="check_website")
]