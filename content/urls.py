from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from .views import ProfilesEndpoint

app_name = "content"

router = SimpleRouter()
router.register(r"profiles", ProfilesEndpoint, basename="profiles")

urlpatterns = []

urlpatterns += router.urls
