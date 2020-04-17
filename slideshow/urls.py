from rest_framework.routers import SimpleRouter
from .views import SlideshowEndpoint, SlideshowPageEndpoint


app_name = "slideshow"
router = SimpleRouter()
router.register(r"slideshow", SlideshowEndpoint)
router.register(r"slideshowpage", SlideshowPageEndpoint)
urlpatterns = []
urlpatterns += router.urls
