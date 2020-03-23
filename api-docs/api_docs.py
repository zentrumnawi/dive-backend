import environ
from django.conf.urls import url
from django.urls import reverse
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# This is the documentation for the API, generated for swagger and Redoc standart
env = environ.Env()
base_url = "https://{}/api".format(
    env("DJANGO_ALLOWED_HOSTS", default="localhost:8000")
)
contact_mail = env("CONTACT_MAIL", default="")
project_name = env("PROJECT_NAME", default="")
schema_view = get_schema_view(
    openapi.Info(
        title="{} API".format(project_name),
        default_version="v1.0",
        description="This is the API for the project {}".format(project_name),
        contact=openapi.Contact(email=contact_mail),
    ),
    # validators=['ssv', 'flex'],
    public=True,
    permission_classes=(permissions.AllowAny,),
    url=base_url,
)

app_name = "api_docs"
urlpatterns = [
    url(
        r"^swagger(?P<format>.json|.yaml)$",
        schema_view.without_ui(cache_timeout=None),
        name="schema-json",
    ),
    url(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=None),
        name="schema-swagger-ui",
    ),
    url(
        r"^redoc/$",
        schema_view.with_ui("redoc", cache_timeout=None),
        name="schema-redoc",
    ),
]
