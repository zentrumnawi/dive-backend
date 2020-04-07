from rest_framework.routers import SimpleRouter
from .views import SlideshowEndpoint


app_name = "slideshow"
router = SimpleRouter()
router.register(r"slideshow", SlideshowEndpoint)
urlpatterns = []
urlpatterns += router.urls
