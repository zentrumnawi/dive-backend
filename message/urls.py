from rest_framework.routers import SimpleRouter
from .views import MessageEndpoint


app_name = "message"
router = SimpleRouter()
router.register(r"message", MessageEndpoint)
urlpatterns = []
urlpatterns += router.urls
