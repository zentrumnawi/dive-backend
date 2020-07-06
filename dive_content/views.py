from django.conf import settings

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.views import APIView, Response
from .models import TreeNode
from .serializers import TreeNodeSerializer


# Create your views here.


class ProfilesEndpoint(ReadOnlyModelViewSet):
    model = TreeNode
    queryset = model.objects.root_nodes()
    serializer_class = TreeNodeSerializer
    name = "profiles"
    app = "api"


class FieldMappingEndpoint(APIView):
    data = settings.DATABASE_FIELD_MAPPING

    def get(self, request):
        return Response(data=self.data)
