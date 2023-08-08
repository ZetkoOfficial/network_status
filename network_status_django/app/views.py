from django.shortcuts import render
from django.http import HttpResponseBadRequest, JsonResponse
from .models import Website, Service
from django.conf import settings as config

from .utils import check_website

def index(request):
    return render(
        request, "index.html", 
        dict(
            websites=Website.objects.all(), 
            services=Service.objects.all(),
            language=config.CONFIG_JSON["language"],
        )
    )

def check_website_view(request):
    if "website_url" not in request.GET: return JsonResponse(dict(check_successful=False))
    
    website_url = request.GET["website_url"]
    if not website_url.startswith("http"): website_url = "http://" + website_url
    return JsonResponse(dict(check_successful=check_website(website_url)))
