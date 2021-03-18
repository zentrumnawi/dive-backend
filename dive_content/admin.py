from django.contrib import admin
from solid_backend.photograph.admin import PhotographInline

from .forms import LeafAdminForm, PlantAdminForm
from .models import Blossom, Fruit, Leaf, Plant, Sprout, ZeigerNumber


leaf_fieldsets = (
    (None, {"fields": ("plant",)}),
    (
        "Blattmerkmale",
        {
            "fields": (
                "veins",
                "division",
                "succulence",
                "texture",
                "cross_section",
                ("attachment", "arrangement"),
                "rosette",
                ("leaf_comp_num", "blade_subdiv_shape"),
                ("incision_num", "incision_depth"),
                (
                    "leaflet_incision_num",
                    "leaflet_incision_add",
                    "leaflet_incision_depth",
                ),
                ("leaf_simple_num", "blade_undiv_shape",),
                "edge",
                "surface",
                "stipule_edge",
                ("base", "apex"),
                "special_features",
                "sheath",
            )
        },
    ),
    ("Keimblattmerkmale", {"fields": ("seed_leaf_num",)}),
)

# Inlines
class LeafInline(admin.StackedInline):
    model = Leaf
    fieldsets = leaf_fieldsets
    form = LeafAdminForm
    classes = ("collapse",)


class BlossomInline(admin.StackedInline):
    model = Blossom
    classes = ("collapse",)


class FruitInline(admin.StackedInline):
    model = Fruit
    classes = ("collapse",)


class SproutInline(admin.StackedInline):
    model = Sprout
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
        BlossomInline,
        FruitInline,
        SproutInline,
        ZeigerNumberInline,
        PhotographInline,
    ]


admin.site.register(Plant, PlantAdmin)


class LeafAdmin(admin.ModelAdmin):
    model = Leaf
    fieldsets = leaf_fieldsets
    form = LeafAdminForm


admin.site.register(Leaf, LeafAdmin)
admin.site.register(Blossom, admin.ModelAdmin)
admin.site.register(Fruit, admin.ModelAdmin)
admin.site.register(Sprout, admin.ModelAdmin)
admin.site.register(ZeigerNumber, admin.ModelAdmin)
