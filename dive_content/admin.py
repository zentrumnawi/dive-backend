from django.contrib import admin
from solid_backend.photograph.admin import PhotographInline

from .forms import (
    BlossomAdminForm,
    BlossomPoalesAdminForm,
    FruitAdminForm,
    IndicatorsAdminForm,
    LeafAdminForm,
    LeafPoalesAdminForm,
    PlantAdminForm,
    StemRhizomePoalesAdminForm,
    StemRootAdminForm,
)
from .models import (
    Blossom,
    BlossomPoales,
    Fruit,
    Indicators,
    Leaf,
    LeafPoales,
    Plant,
    StemRhizomePoales,
    StemRoot,
)

plant_fieldsets = (
    (None, {"fields": (("tree_node", "taxonomy"),)}),
    (
        None,
        {
            "fields": (
                "short_description",
                "subsection_title_general",
                "name",
                "article_trivial_name",
                "alternative_trivial_names",
                ("growth_form", "growth_height"),
                ("interaction", "dispersal"),
                "ground",
                ("habitats", "ruderal_sites"),
                ("life_form", "status"),
                "other_features",
                "output_general",
            )
        },
    ),
)

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

blossompoales_fieldsets = (
    (None, {"fields": ("plant",)}),
    (
        None,
        {
            "fields": (
                "subsection_title_season",
                "season",
                "output_season",
                "subsection_title_inflorescence",
                (
                    "inflorescence_blossom_number",
                    "inflorescence_density",
                    "inflorescence_position",
                ),
                ("inflorescence_type", "inflorescence_features"),
                ("inflorescence_bract_length", "inflorescence_bract_feature"),
                "output_inflorescence",
                "subsection_title_blossom_perianth",
                ("blossom_sex", "perianth"),
                "blossom_description",
                "perianth_description",
                "output_blossom_perianth",
                "subsection_title_spikelet",
                ("spikelet_length", "spikelet_shape", "spikelet_attachment"),
                ("spikelet_sex", "spikelet_blossom_number"),
                "spikelet_max_width",
                ("spikelet_rachilla", "spikelet_stalk", "spikelet_spindle"),
                "spikelet_features",
                "output_spikelet",
                "subsection_title_husks",
                ("husks_form", "husks_keel", "husks_cross_section"),
                "husks_description",
                "output_husks",
            )
        },
    ),
)
blossompoales_radio_fields = {
    "inflorescence_density": admin.VERTICAL,
    "inflorescence_position": admin.VERTICAL,
    "inflorescence_type": admin.HORIZONTAL,
    "blossom_sex": admin.VERTICAL,
    "perianth": admin.VERTICAL,
    "spikelet_sex": admin.HORIZONTAL,
    "spikelet_max_width": admin.HORIZONTAL,
    "husks_form": admin.VERTICAL,
    "husks_keel": admin.VERTICAL,
}

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

stemrhizomepoales_fieldsets = (
    (None, {"fields": ("plant",)}),
    (
        None,
        {
            "fields": (
                "subsection_title_growth_form",
                "tuft_stolon",
                "output_growth_form",
                "subsection_title_stem",
                "stem_color",
                ("stem_hairiness", "stem_cross_section"),
                "stem_pith",
                ("stem_nodes", "stem_nodes_hairiness"),
                "stem_transverse_walls",
                "stem_surface",
                "stem_features",
                "output_stem",
                "subsection_title_rhizome",
                "rhizome_length",
                "rhizome_branching",
                "output_rhizome",
            )
        },
    ),
)
stemrhizomepoales_radio_fields = {
    "stem_hairiness": admin.VERTICAL,
    "stem_pith": admin.HORIZONTAL,
    "stem_nodes": admin.VERTICAL,
    "stem_nodes_hairiness": admin.VERTICAL,
    "stem_transverse_walls": admin.HORIZONTAL,
    "rhizome_length": admin.HORIZONTAL,
    "rhizome_branching": admin.HORIZONTAL,
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


class LeafPoalesInline(admin.StackedInline):
    model = LeafPoales
    fieldsets = leafpoales_fieldsets
    form = LeafPoalesAdminForm
    radio_fields = leafpoales_radio_fields
    classes = ("collapse",)


class BlossomInline(admin.StackedInline):
    model = Blossom
    fieldsets = blossom_fieldsets
    form = BlossomAdminForm
    classes = ("collapse",)


class BlossomPoalesInline(admin.StackedInline):
    model = BlossomPoales
    fieldsets = blossompoales_fieldsets
    form = BlossomPoalesAdminForm
    radio_fields = blossompoales_radio_fields
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


class StemRhizomePoalesInline(admin.StackedInline):
    model = StemRhizomePoales
    fieldsets = stemrhizomepoales_fieldsets
    form = StemRhizomePoalesAdminForm
    radio_fields = stemrhizomepoales_radio_fields
    classes = ("collapse",)


class IndicatorsInline(admin.StackedInline):
    model = Indicators
    fieldsets = indicators_fieldsets
    form = IndicatorsAdminForm
    readonly_fields = indicators_readonly_fields
    classes = ("collapse",)


class PlantAdmin(admin.ModelAdmin):
    fieldsets = plant_fieldsets
    form = PlantAdminForm
    readonly_fields = ("taxonomy",)
    list_display = ("id", "name_without_markdown_symbols", "trivial_name")
    list_display_links = ("name_without_markdown_symbols",)
    inlines = [
        LeafInline,
        LeafPoalesInline,
        BlossomInline,
        BlossomPoalesInline,
        FruitInline,
        StemRootInline,
        StemRhizomePoalesInline,
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


class BlossomPoalesAdmin(admin.ModelAdmin):
    model = BlossomPoales
    fieldsets = blossompoales_fieldsets
    form = BlossomPoalesAdminForm
    radio_fields = blossompoales_radio_fields


admin.site.register(BlossomPoales, BlossomPoalesAdmin)


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


class StemRhizomePoalesAdmin(admin.ModelAdmin):
    model = StemRhizomePoales
    fieldsets = stemrhizomepoales_fieldsets
    form = StemRhizomePoalesAdminForm
    radio_fields = stemrhizomepoales_radio_fields


admin.site.register(StemRhizomePoales, StemRhizomePoalesAdmin)


class IndicatorsAdmin(admin.ModelAdmin):
    model = Indicators
    fieldsets = indicators_fieldsets
    form = IndicatorsAdminForm
    readonly_fields = indicators_readonly_fields


admin.site.register(Indicators, IndicatorsAdmin)
