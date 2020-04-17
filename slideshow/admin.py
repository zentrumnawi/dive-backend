from django.contrib import admin
from .models import Slideshow, SlideshowPage, SlideshowImage
from utility.forms import HasImgForm


admin.site.register(Slideshow, admin.ModelAdmin)


class SlideshowPageAdmin(admin.ModelAdmin):
    list_display = ["id", "show", "position", "title"]

admin.site.register(SlideshowPage, SlideshowPageAdmin)


class SlideshowImageAdmin(admin.ModelAdmin):
    form = HasImgForm
    list_display = ["id", "page", "position", "title", "img"]

admin.site.register(SlideshowImage, SlideshowImageAdmin)
