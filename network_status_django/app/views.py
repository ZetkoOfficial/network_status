from django.shortcuts import render
from .models import Website, Service
from django.conf import settings as config

def index(request):
    return render(
        request, "index.html", 
        dict(
            websites=Website.objects.all(), 
            services=Service.objects.all(),
            language=config.CONFIG_JSON["language"],
        )
    )