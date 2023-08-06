import datetime

from django.utils import timezone
from django.test import TestCase
from django.conf import settings as config
from django.urls import reverse

from .models import Website, Service


class ConfigTests(TestCase):
    def test_int_only(self):
        self.assertIsInstance(config.CONFIG_JSON["default_check_interval"], int)
        self.assertIsInstance(config.CONFIG_JSON["timeout"], int)

class WebsiteTests(TestCase):
    def test_website_first_run(self):
        website = Website(website_name="test", website_url="https://example.invalid", check_interval=10)
        website.current_status = True

        self.assertFalse(website.check_time())

    def test_website_not_yet(self):
        time = timezone.now() - datetime.timedelta(minutes=8)
        website = Website(website_name="test", website_url="https://example.invalid", check_interval=10)
        website.current_status = True; website.last_checked = time

        self.assertTrue(website.check_time())

    def test_website_check_now(self):
        time = timezone.now() - datetime.timedelta(minutes=13)
        website = Website(website_name="test", website_url="https://example.invalid", check_interval=10)
        website.current_status = True; website.last_checked = time

        self.assertFalse(website.check_time())
    
    def test_valid_website(self):
        website = Website(website_name="test", website_url="https://example.com", check_interval=10)
        
        self.assertTrue(website.check_time())

class ServiceTests(TestCase):
    def test_service_first_run(self):
        service = Service(service_name="test", service_type="test", service_ip="123.456.0.789", check_interval=10)
        service.current_status = True

        self.assertFalse(service.check_time())

    def test_website_not_yet(self):
        time = timezone.now() - datetime.timedelta(minutes=2)
        service = Service(service_name="test", service_type="test", service_ip="123.456.0.789", check_interval=10)
        service.current_status = True; service.last_checked = time

        self.assertTrue(service.check_time())

    def test_website_check_now(self):
        time = timezone.now() - datetime.timedelta(minutes=33)
        service = Service(service_name="test", service_type="test", service_ip="123.456.0.789", check_interval=10)
        service.current_status = True; service.last_checked = time

        self.assertFalse(service.check_time())
    
    def test_valid_service(self):
        service = Service(service_name="test", service_type="test", service_ip="127.0.0.1", check_interval=10)
        
        self.assertTrue(service.check_time())

class DisplayTests(TestCase):
    def test_empty_all(self):
        response = self.client.get(reverse("index"))
        self.assertContains(response, config.CONFIG_JSON["language"]["empty"], 2)
    def test_one_website(self):
        website = Website.objects.create(website_name="889475395386838378735", website_url="https://example.invalid", check_interval=10)
        response = self.client.get(reverse("index"))

        self.assertContains(response, "889475395386838378735")
        self.assertContains(response, "https://example.invalid")
    def test_one_service(self):
        service = Service.objects.create(service_name="48758648956936563", service_type="847865894695649", service_ip="123.456.0.789", check_interval=10)
        response = self.client.get(reverse("index"))

        self.assertContains(response, "48758648956936563(847865894695649)")
        self.assertContains(response, "123.456.0.789")