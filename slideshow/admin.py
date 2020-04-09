from django.contrib import admin
from .models import Slideshow, SlideshowPage


admin.site.register(Slideshow, admin.ModelAdmin)
admin.site.register(SlideshowPage, admin.ModelAdmin)
