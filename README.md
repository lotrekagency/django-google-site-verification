# django-google-site-verification

Our internal utility to easily add Google verification file

## Install

    pip install google_site_verification

## Usage

Include google_site_verification in your INSTALLED_APPS

INSTALLED_APPS = [
    'google_site_verification',
]

To setup your google site verification html file just add to your settings

    GOOGLE_SITE_VERIFICATION_FILE = "google11a50bcc62df11b5.html"

and import GOOGLE_SITE_VERIFICATION_URL in your URLConf

    from django.conf.urls import url
    from google_site_verification import GOOGLE_SITE_VERIFICATION_URL

    from . import views


    urlpatterns = [
        url(r'^$', views.home, name='home'),
        GOOGLE_SITE_VERIFICATION_URL
    ]


## Run tests

    $ pip install -r requirements-dev.txt
    $ ./runtests.py --with-coverage