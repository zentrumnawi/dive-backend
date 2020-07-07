from django.contrib import admin
from solid_backend.photograph.admin import PhotographInline

from .models import Plant, Leaf, Sprout, Fruit, Blossom
from .forms import PlantModelForm


# Inlines
class LeafInline(admin.StackedInline):
    model = Leaf


class SproutInline(admin.StackedInline):
    model = Sprout


class FruitInline(admin.StackedInline):
    model = Fruit


class BlossomInline(admin.StackedInline):
    model = Blossom


class PlantModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "trivial_name")
    form = PlantModelForm
    inlines = [LeafInline, SproutInline, FruitInline, BlossomInline, PhotographInline]


admin.site.register(Leaf, admin.ModelAdmin)
admin.site.register(Sprout, admin.ModelAdmin)
admin.site.register(Fruit, admin.ModelAdmin)
admin.site.register(Blossom, admin.ModelAdmin)
admin.site.register(Plant, PlantModelAdmin)
