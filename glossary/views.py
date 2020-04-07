from .models import GlossaryEntry
from .serializers import GlossaryEntrySerializer
from rest_framework.viewsets import ReadOnlyModelViewSet


class GlossaryEntryEndpoint(ReadOnlyModelViewSet):
    queryset = GlossaryEntry.objects.all()
    serializer_class = GlossaryEntrySerializer
    name = "glossaryentry"
