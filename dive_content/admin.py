from django.contrib import admin
from solid_backend.photograph.admin import PhotographInline

from .forms import PlantModelForm
from .models import Blossom, Fruit, Leaf, Plant, Sprout, ZeigerNumber


# Inlines
class LeafInline(admin.StackedInline):
    model = Leaf


class SproutInline(admin.StackedInline):
    model = Sprout


class FruitInline(admin.StackedInline):
    model = Fruit


class BlossomInline(admin.StackedInline):
    model = Blossom


class ZeigerNumberInline(admin.StackedInline):
    model = ZeigerNumber


class PlantAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "trivial_name")
    form = PlantModelForm
    inlines = [
        LeafInline,
        SproutInline,
        FruitInline,
        BlossomInline,
        ZeigerNumberInline,
        PhotographInline,
    ]


admin.site.register(Leaf, admin.ModelAdmin)
admin.site.register(Sprout, admin.ModelAdmin)
admin.site.register(Fruit, admin.ModelAdmin)
admin.site.register(Blossom, admin.ModelAdmin)
admin.site.register(Plant, PlantAdmin)
admin.site.register(ZeigerNumber, admin.ModelAdmin)
