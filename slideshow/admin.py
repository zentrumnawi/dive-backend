from django.contrib import admin
from .models import Slideshow, SlideshowPage, SlideshowImage
from utility.forms import HasImgAltForm


admin.site.register(Slideshow, admin.ModelAdmin)
admin.site.register(SlideshowPage, admin.ModelAdmin)


class SlideshowImageAdmin(admin.ModelAdmin):
    form = HasImgAltForm
    list_display = ["id", "page", "position", "title", "img", "img_alt"]

admin.site.register(SlideshowImage, SlideshowImageAdmin)
