from django.contrib import admin
from solid_backend.photograph.admin import PhotographInline

from .forms import FruitAdminForm, LeafAdminForm, PlantAdminForm, StemRootAdminForm
from .models import Blossom, Fruit, Leaf, Plant, StemRoot, ZeigerNumber

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
leaf_radio_fields = {"rosette": admin.HORIZONTAL, "seed_leaf_num": admin.HORIZONTAL}

fruit_fieldsets = (
    (None, {"fields": ("plant",)}),
    (
        None,
        {
            "fields": (
                ("fruit_form", "fruit_type"),
                "ovule_pos",
                ("seed_num", "seed_form"),
                ("winging", "winging_feature"),
            )
        },
    ),
)
fruit_radio_fields = {"ovule_pos": admin.HORIZONTAL}

stemroot_fieldsets = (
    (None, {"fields": ("plant",)}),
    (
        "Sprossmerkmale",
        {
            "fields": (
                "orientation",
                "appearance",
                "succulence",
                "cross_section",
                "surface",
                "creep_lay_shoots",
                "runners",
                "bracts",
                "milky_sap",
            )
        },
    ),
    (
        "Wurzeln und unterirdische Planzenorgane",
        {"fields": ("organ_features", "organs", "primary_root")},
    ),
)
stemroot_radio_fields = {
    "succulence": admin.HORIZONTAL,
    "creep_lay_shoots": admin.HORIZONTAL,
    "runners": admin.HORIZONTAL,
    "bracts": admin.HORIZONTAL,
    "primary_root": admin.HORIZONTAL,
}

# Inlines
class LeafInline(admin.StackedInline):
    model = Leaf
    fieldsets = leaf_fieldsets
    form = LeafAdminForm
    radio_fields = leaf_radio_fields
    classes = ("collapse",)


class BlossomInline(admin.StackedInline):
    model = Blossom
    classes = ("collapse",)


class FruitInline(admin.StackedInline):
    model = Fruit
    fieldsets = fruit_fieldsets
    form = FruitAdminForm
    radio_fields = fruit_radio_fields
    classes = ("collapse",)


class StemRootInline(admin.StackedInline):
    model = StemRoot
    fieldsets = stemroot_fieldsets
    form = StemRootAdminForm
    radio_fields = stemroot_radio_fields
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
        StemRootInline,
        ZeigerNumberInline,
        PhotographInline,
    ]


admin.site.register(Plant, PlantAdmin)


class LeafAdmin(admin.ModelAdmin):
    model = Leaf
    fieldsets = leaf_fieldsets
    form = LeafAdminForm
    radio_fields = leaf_radio_fields


admin.site.register(Leaf, LeafAdmin)
admin.site.register(Blossom, admin.ModelAdmin)


class FruitAdmin(admin.ModelAdmin):
    model = Fruit
    fieldsets = fruit_fieldsets
    form = FruitAdminForm
    radio_fields = fruit_radio_fields


admin.site.register(Fruit, FruitAdmin)


class StemRootAdmin(admin.ModelAdmin):
    model = StemRoot
    fieldsets = stemroot_fieldsets
    form = StemRootAdminForm
    radio_fields = stemroot_radio_fields


admin.site.register(StemRoot, StemRootAdmin)
admin.site.register(ZeigerNumber, admin.ModelAdmin)
