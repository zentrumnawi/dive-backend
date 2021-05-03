"""djangodocker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    url(r'^admin/', admin.site.urls),
]"""

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    url(
        r"^{}".format(settings.URI_PREFIX),
        include("api_docs.api_docs"),
        name="api_docs",
    ),
    url(r"^{}".format(settings.URI_PREFIX), include("solid_backend.urls")),
    url(r"^{}admin/".format(settings.URI_PREFIX), admin.site.urls),
]
