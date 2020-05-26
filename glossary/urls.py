from rest_framework.routers import SimpleRouter
from .views import GlossaryEntryEndpoint


app_name = "glossary"
router = SimpleRouter()
router.register(r"glossaryentries", GlossaryEntryEndpoint)
urlpatterns = []
urlpatterns += router.urls
