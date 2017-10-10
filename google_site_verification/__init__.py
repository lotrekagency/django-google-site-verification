from django.conf import settings
from django.conf.urls import url
from .views import google_site_verification_view


GOOGLE_SITE_VERIFICATION_URL = url(
    r'^{0}$'.format(getattr(settings, "GOOGLE_SITE_VERIFICATION_FILE", '')), 
    google_site_verification_view, name='google_site_verification'
)