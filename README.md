# django-google-site-verification
[![Latest Version](https://img.shields.io/pypi/v/google-site-verification.svg)](https://pypi.python.org/pypi/google-site-verification/)
[![codecov](https://codecov.io/gh/lotrekagency/django-google-site-verification/branch/master/graph/badge.svg)](https://codecov.io/gh/lotrekagency/django-google-site-verification)
[![Build Status](https://travis-ci.org/lotrekagency/django-google-site-verification.svg?branch=master)](https://travis-ci.org/lotrekagency/django-google-site-verification)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/Owanesh/google-site-verification/blob/master/LICENSE)

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
