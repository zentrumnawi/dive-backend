from rest_framework import generics, status, response
from django.core.mail import send_mail
from drf_yasg.utils import swagger_auto_schema
from config.settings.common import env
from .serializers import ContactSerializer


class ContactView(generics.GenericAPIView):
    serializer_class = ContactSerializer

    permission_classes = ()

    @swagger_auto_schema(responses={200: "The views response is 200 if mail is sent"})
    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data

        message = send_mail(
            subject=data["subject"],
            message=data["message"],
            from_email="{0} <{1}>".format(serializer["name"], data["email"]),
            recipient_list=[env.str("SYSTEM_EMAIL")],
            fail_silently=False,
        )
        if not message:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)
        return response.Response(data=serializer)
