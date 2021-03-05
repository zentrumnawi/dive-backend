from django.contrib import admin
from solid_backend.photograph.admin import PhotographInline

from .forms import PlantAdminForm
from .models import Blossom, Fruit, Leaf, Plant, Sprout, ZeigerNumber


# Inlines
class LeafInline(admin.StackedInline):
    model = Leaf
    classes = ("collapse",)


class SproutInline(admin.StackedInline):
    model = Sprout
    classes = ("collapse",)


class FruitInline(admin.StackedInline):
    model = Fruit
    classes = ("collapse",)


class BlossomInline(admin.StackedInline):
    model = Blossom
    classes = ("collapse",)


class ZeigerNumberInline(admin.StackedInline):
    model = ZeigerNumber
    classes = ("collapse",)


class PlantAdmin(admin.ModelAdmin):
    form = PlantAdminForm
    readonly_fields = ("taxonomy", "get_ground_output")
    list_display = ("id", "name", "trivial_name")
    list_display_links = ("name",)
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
