from django.contrib import admin
from .models import Slideshow


admin.site.register(Slideshow, admin.ModelAdmin)
