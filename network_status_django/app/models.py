from django.db import models
from django.utils import timezone
from django.conf import settings as config

from .utils import check_website, check_service

class StatusModel(models.Model):
    current_status  = models.BooleanField("current status", default=False, editable=False)
    last_checked    = models.DateTimeField("last time of checking status", default=timezone.datetime(2000,1,1,tzinfo=timezone.get_current_timezone()),editable=False)
    check_interval  = models.PositiveIntegerField("check interval in minutes", default=config.CONFIG_JSON["default_check_interval"])

    class Meta:
        abstract = True

    def _check_online(self):
        pass

    def check_time(self):
        time = timezone.now()
        if (time-self.last_checked).total_seconds()/60 >= self.check_interval:
            self.last_checked = time
            self.save()
            self.current_status = self._check_online()
            self.save()

        return self.current_status


class Website(StatusModel):
    website_name    = models.CharField("website name", max_length=50)
    website_url     = models.URLField("website URL")

    def _check_online(self): return check_website(self.website_url)
        
    def __str__(self):
        return f"{self.website_name}@{self.website_url}"
    
class Service(StatusModel):
    service_name    = models.CharField("service name", max_length=50)
    service_type    = models.CharField("service type", max_length=50)
    service_ip      = models.GenericIPAddressField("service IP")

    def _check_online(self): return check_service(self.service_ip)
    
    def __str__(self):
        return f"{self.service_name}@{self.service_ip}"