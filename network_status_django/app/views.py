from django.shortcuts import render
from django.http import HttpResponseBadRequest, JsonResponse, HttpResponse
from .models import Website, Service
from django.conf import settings as config

from .utils import check_website, generate_random_data

def index(request):
    return render(
        request, "index.html", 
        dict(
            websites=Website.objects.all(), 
            services=Service.objects.all(),
            size=config.CONFIG_JSON["speedtest_size_MB"],
            language=config.CONFIG_JSON["language"],
            allow_manual_search=config.CONFIG_JSON["allow_manual_search"],
        )
    )

def random(request):
    random_data = generate_random_data(config.CONFIG_JSON["speedtest_size_MB"])
    response = HttpResponse(random_data, content_type="application/octet-stream")
    return response

def check_website_view(request):
    if "website_url" not in request.GET: return JsonResponse(dict(check_successful=False))
    
    website_url = request.GET["website_url"]
    if not website_url.startswith("http"): website_url = "http://" + website_url
    return JsonResponse(dict(check_successful=check_website(website_url)))
