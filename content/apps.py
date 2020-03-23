from importlib import import_module

from django.apps import AppConfig
from django.conf import settings


class ContentConfig(AppConfig):
    name = "content"
    profiles_serializer = None

    def ready(self):

        module_ser_class = settings.PROFILES_SERIALIZER.rsplit(".", 1) or None
        # raise Exception(module_ser_class)
        if any(module_ser_class):
            self.profiles_serializer = getattr(import_module(module_ser_class[0]), module_ser_class[1])(many=True)
