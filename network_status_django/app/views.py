from django.shortcuts import render
from .models import Website, Service

def index(request):
    return render(request, "index.html", dict(websites=Website.objects.all(), services=Service.objects.all()))