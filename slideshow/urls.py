from rest_framework.routers import SimpleRouter
from .views import SlideshowEndpoint, SlideshowPageEndpoint, SlideshowImageEndpoint


app_name = "slideshow"
router = SimpleRouter()
router.register(r"slideshows", SlideshowEndpoint)
router.register(r"slideshowpages", SlideshowPageEndpoint)
router.register(r"slideshowimages", SlideshowImageEndpoint)
urlpatterns = []
urlpatterns += router.urls
