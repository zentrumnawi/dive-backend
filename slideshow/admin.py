from django.contrib import admin
from .models import Slideshow, SlideshowPage, SlideshowImage
from utility.forms import HasImgForm


class SlideshowPageInline(admin.TabularInline):
    model = SlideshowPage


class SlideshowImageInline(admin.TabularInline):
    model = SlideshowImage


class SlideshowAdmin(admin.ModelAdmin):
    list_display = ["title"]
    inlines = [SlideshowPageInline]

admin.site.register(Slideshow, SlideshowAdmin)


class SlideshowPageAdmin(admin.ModelAdmin):
    list_display = ["id", "show", "position", "title"]
    inlines = [SlideshowImageInline]

admin.site.register(SlideshowPage, SlideshowPageAdmin)


class SlideshowImageAdmin(admin.ModelAdmin):
    form = HasImgForm
    list_display = ["id", "page", "position", "title", "img"]

admin.site.register(SlideshowImage, SlideshowImageAdmin)
