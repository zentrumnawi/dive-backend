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

urlpatterns = [
    url(r"^api/", include("api-docs.api_docs"), name="api_docs"),
    url(r"^api/", include("content.urls"), name="content"),
    url(r"^admin/", admin.site.urls),
    url(r"api/", include("glossary.urls", namespace="glossary")),
    url(r"api/", include("quiz.urls", namespace="quiz")),
    url(r"^api/", include("message.urls"), name="message"),
    url(r"api/", include("slideshow.urls"), name="slideshow"),
]
