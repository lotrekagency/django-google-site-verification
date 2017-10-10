from django.conf import settings
from django.shortcuts import render


def google_verification_view(request):
    google_site_ver = getattr(settings, "GOOGLE_SITE_VERIFICATION_FILE", None)
    context = {
        'google_site_ver' : google_site_ver
    }
    return render(
        'google-site-verification/google_verification.html',
        context, content_type='text/html'
    )