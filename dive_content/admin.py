from django.contrib import admin
from solid_backend.photograph.admin import PhotographInline

from .forms import (
    BlossomAdminForm,
    FruitAdminForm,
    IndicatorsAdminForm,
    LeafAdminForm,
    LeafPoalesAdminForm,
    PlantAdminForm,
    StemRootAdminForm,
)
from .models import Blossom, Fruit, Indicators, Leaf, LeafPoales, Plant, StemRoot

leaf_fieldsets = (
    (None, {"fields": ("plant",)}),
    (
        "Blattmerkmale",
        {
            "fields": (
                "color",
                "veins",
                "division",
                "succulence",
                "texture",
                "cross_section",
                ("attachment", "arrangement"),
                "rosette",
                (
                    "leaf_comp_num",
                    "leaf_comp_blade_shape",
                    "leaf_comp_incision_num",
                    "leaf_comp_incision_depth",
                ),
                (
                    "leaflet_incision_num",
                    "leaflet_incision_add",
                    "leaflet_incision_depth",
                ),
                (
                    "leaf_simple_num",
                    "leaf_simple_blade_shape",
                    "leaf_simple_incision_num",
                    "leaf_simple_incision_depth",
                ),
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

leafpoales_fieldsets = (
    (None, {"fields": ("plant",)}),
    (
        None,
        {
            "fields": (
                "subsection_title_overview",
                ("length", "width", "color"),
                ("shape", "hairiness", "cross_section"),
                ("alignment", "attachment_point"),
                "output_overview",
                "subsection_title_leaf_blade",
                ("blade_shape", "blade_shape_feature"),
                ("blade_corrugation", "blade_double_groove"),
                ("blade_shine", "blade_keel"),
                "blade_edge",
                "blade_bud_system",
                "output_leaf_blade",
                "subsection_title_leaf_base",
                ("base_edge", "base_auricle", "base_auricle_feature"),
                "output_leaf_base",
                "subsection_title_ligule",
                ("ligule_length", "ligule_color"),
                ("ligule_shape", "ligule_consistency"),
                "ligule_features",
                "output_ligule",
                "subsection_title_leaf_sheath",
                ("sheath_coloring", "sheath_connation"),
                "sheath_features",
                "output_leaf_sheath",
            )
        },
    ),
)
leafpoales_radio_fields = {
    "shape": admin.VERTICAL,
    "attachment_point": admin.HORIZONTAL,
    "blade_double_groove": admin.VERTICAL,
    "blade_keel": admin.HORIZONTAL,
    "blade_bud_system": admin.HORIZONTAL,
    "base_edge": admin.VERTICAL,
    "base_auricle": admin.VERTICAL,
}

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
)

fruit_fieldsets = (
    (None, {"fields": ("plant",)}),
    (
        None,
        {
            "fields": (
                ("fruit_form", "fruit_type"),
                "ovule_pos",
                ("seed_num", "seed_color_form"),
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
                "pith",
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
    "pith": admin.HORIZONTAL,
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
    fields = (
        ("tree_node", "taxonomy"),
        "name",
        ("article", "trivial_name"),
        "short_description",
        "alt_trivial_name",
        ("habitat", "ground"),
        "status",
        "interaction",
        ("life_form", "growth_form", "growth_height"),
        "dispersal",
        "other_features",
    )
    form = PlantAdminForm
    readonly_fields = ("taxonomy",)
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


class LeafPoalesAdmin(admin.ModelAdmin):
    model = LeafPoales
    fieldsets = leafpoales_fieldsets
    form = LeafPoalesAdminForm
    radio_fields = leafpoales_radio_fields


admin.site.register(LeafPoales, LeafPoalesAdmin)


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
