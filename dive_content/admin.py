from django.contrib import admin
from solid_backend.photograph.admin import PhotographInline

from .forms import (
    BlossomAdminForm,
    FruitAdminForm,
    IndicatorsAdminForm,
    LeafAdminForm,
    PlantAdminForm,
    StemRootAdminForm,
)
from .models import Blossom, Fruit, Indicators, Leaf, Plant, StemRoot

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

blossom_fieldsets = (
    (None, {"fields": ("plant",)}),
    (
        "Blütenmerkmale",
        {
            "fields": (
                "season",
                ("inflorescence_num", "inflorescence_type", "blossom_num"),
                ("merosity", "symmetry", "perianth"),
                "perianth_form",
                "bract_blade",
                "diameter",
                ("sepal_num", "sepal_color_form"),
                ("sepal_connation_type", "sepal_connation"),
                "epicalyx",
                ("petal_num", "petal_len", "petal_color_form"),
                ("petal_connation_type", "petal_connation"),
                "nectary",
                ("stamen_num", "stamen_len", "stamen_color_form"),
                ("stamen_connation_type", "stamen_connation_type_add"),
                ("carpel_num", "carpel_connation_type", "ovary_pos"),
                "pistil_pos",
                "stigma_num",
                "stylopodium",
            )
        },
    ),
    (
        "Sonderform Poales",
        {
            "fields": (
                "grann_top",
                "grann_form",
                "cons_top",
                "gull_spel",
                "blos",
                "straw_ground",
                "order",
                "aer_per_aer",
                "aer_per_ab",
            )
        },
    ),
)

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

indicators_fieldsets = (
    (None, {"fields": ("plant", "not_specified")}),
    (None, {"fields": ("light", "temperature", "humidity", "reaction", "nitrogen")}),
    (None, {"fields": ("get_key",)}),
)
indicators_readonly_fields = ("get_key",)

# Inlines
class LeafInline(admin.StackedInline):
    model = Leaf
    fieldsets = leaf_fieldsets
    form = LeafAdminForm
    radio_fields = leaf_radio_fields
    classes = ("collapse",)


class BlossomInline(admin.StackedInline):
    model = Blossom
    fieldsets = blossom_fieldsets
    form = BlossomAdminForm
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


class IndicatorsInline(admin.StackedInline):
    model = Indicators
    fieldsets = indicators_fieldsets
    form = IndicatorsAdminForm
    readonly_fields = indicators_readonly_fields
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
        IndicatorsInline,
        PhotographInline,
    ]


admin.site.register(Plant, PlantAdmin)


class LeafAdmin(admin.ModelAdmin):
    model = Leaf
    fieldsets = leaf_fieldsets
    form = LeafAdminForm
    radio_fields = leaf_radio_fields


admin.site.register(Leaf, LeafAdmin)


class BlossomAdmin(admin.ModelAdmin):
    model = Blossom
    fieldsets = blossom_fieldsets
    form = BlossomAdminForm


admin.site.register(Blossom, BlossomAdmin)


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


class IndicatorsAdmin(admin.ModelAdmin):
    model = Indicators
    fieldsets = indicators_fieldsets
    form = IndicatorsAdminForm
    readonly_fields = indicators_readonly_fields


admin.site.register(Indicators, IndicatorsAdmin)
