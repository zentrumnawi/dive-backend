from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from .views import ProfilesEndpoint, FieldMappingEndpoint

app_name = "content"

router = SimpleRouter()
router.register(r"profiles", ProfilesEndpoint, basename="profiles")

urlpatterns = [
    url(r"field-mapping", FieldMappingEndpoint.as_view(), name="field-mapping"),
]

urlpatterns += router.urls
