from rest_framework.routers import SimpleRouter
from .views import MessageEndpoint


app_name = "message"
router = SimpleRouter()
router.register(r"messages", MessageEndpoint)
urlpatterns = []
urlpatterns += router.urls
