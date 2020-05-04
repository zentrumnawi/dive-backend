from .models import GlossaryEntry
from .serializers import GlossaryEntrySerializer
from rest_framework.viewsets import ReadOnlyModelViewSet


class GlossaryEntryEndpoint(ReadOnlyModelViewSet):
    """
    Endpoint that provides the database table of all glossary entries.
    """

    queryset = GlossaryEntry.objects.all()
    serializer_class = GlossaryEntrySerializer
    name = "glossaryentry"
