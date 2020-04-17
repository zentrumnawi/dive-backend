from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Slideshow, SlideshowPage
from .serializers import SlideshowSerializer, SlideshowPageSerializer


class SlideshowEndpoint(ReadOnlyModelViewSet):
    """
    Endpoint that provides the database table of all Slideshows including their
    pages and images.
    """
    
    queryset = Slideshow.objects.all()
    serializer_class = SlideshowSerializer
    name = "slideshow"


class SlideshowPageEndpoint(ReadOnlyModelViewSet):
    """
    Endpoint that provides the database table of all SlideshowPages including
    their images.
    """

    queryset = SlideshowPage.objects.all()
    serializer_class = SlideshowPageSerializer
    name = "slideshowpage"

