from django.conf.urls import url

from .views import google_verification_view

urlpatterns = [
    url(r'^$', google_verification_view, name='google_verification_view'),
]