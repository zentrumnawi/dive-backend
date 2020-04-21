from rest_framework.viewsets import ReadOnlyModelViewSet
from datetime import date
from .models import Message
from .serializers import MessageSerializer


class MessageEndpoint(ReadOnlyModelViewSet):
    """
    Endpoint that provides the database table of currently valid Messages.
    """

    queryset = Message.objects.filter(
        valid_from__lte=date.today(), valid_to__gte=date.today()
    )
    serializer_class = MessageSerializer
    name = "message"
