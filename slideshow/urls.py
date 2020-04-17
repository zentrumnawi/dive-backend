from rest_framework.routers import SimpleRouter
from .views import SlideshowEndpoint, SlideshowPageEndpoint, SlideshowImageEndpoint


app_name = "slideshow"
router = SimpleRouter()
router.register(r"slideshow", SlideshowEndpoint)
router.register(r"slideshowpage", SlideshowPageEndpoint)
router.register(r"slideshowimage", SlideshowImageEndpoint)
urlpatterns = []
urlpatterns += router.urls
