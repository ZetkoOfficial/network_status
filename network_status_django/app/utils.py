import requests
import subprocess
from django.conf import settings as config

def check_website(website_url):
    try:
        r = requests.head(website_url, timeout=config.CONFIG_JSON["timeout"], verify=True)
        return (r.status_code >= 200 and r.status_code < 400)
    except:
        return False
    
def check_service(service_ip):
    try:
        result = subprocess.call(['ping', '-c', '1', '-w', str(config.CONFIG_JSON["timeout"]), service_ip], stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        return result == 0
    except:
        return False