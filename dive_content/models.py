from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _
from solid_backend.content.models import BaseProfile

from .choices import *

# Custom models, representing the actual data of a profile, implement here.
# One model and only one needs to inherit form the BaseProfil model to get a relation
# to the TreeNode model that provides a tree structure to repesent the systematics of
# the profiles.


class Plant(BaseProfile):
    BaseProfile._meta.get_field("tree_node").verbose_name = _("Steckbrief-Ebene")
    short_description = models.TextField(
        default="",
        max_length=600,
        blank=True,
        verbose_name=_("Kurzbeschreibung"),
        help_text=_("Markdown"),
    )
    # general (sentence 1) -------------------------------------------------------------
    name = models.CharField(
        max_length=100, verbose_name=_("Art"), help_text=_("Markdown")
    )
    article = models.CharField(
        max_length=3, choices=ARTICLE_CHOICES, blank=True, verbose_name=_("Artikel")
    )
    trivial_name = models.CharField(max_length=50, verbose_name=_("Trivialname"))
    alternative_trivial_names = ArrayField(
        base_field=models.CharField(max_length=50),
        size=4,
        blank=True,
        default=list,
        verbose_name=_("Alternative Trivialnamen"),
    )
    growth_form = models.CharField(
        max_length=3,
        choices=GROWTH_FORM_CHOICES,
        blank=True,
        verbose_name=_("Wuchsform"),
    )
    growth_height = models.CharField(
        max_length=20, blank=True, verbose_name=_("Wuchshöhe")
    )
    # general (sentence 2) -------------------------------------------------------------
    interaction = models.CharField(
        max_length=3,
        choices=INTERACTION_CHOICES,
        blank=True,
        verbose_name=_("Interaktion"),
    )
    dispersal_form = models.CharField(
        max_length=2,
        choices=DISPERSAL_FORM_CHOICES,
        blank=True,
        verbose_name=_("Ausbreitungsform"),
    )
    ground = models.PositiveSmallIntegerField(
        choices=GROUND_CHOICES, blank=True, null=True, verbose_name=_("Untergrund")
    )
    habitats = ArrayField(
        base_field=models.PositiveSmallIntegerField(choices=HABITATS_CHOICES),
        blank=True,
        default=list,
        verbose_name=_("Habitate"),
    )
    ruderal_sites = ArrayField(
        base_field=models.PositiveSmallIntegerField(choices=RUDERAL_SITES_CHOICES),
        blank=True,
        default=list,
        verbose_name=_("Ruderalstandorte"),
    )
    # general (sentence 3) -------------------------------------------------------------
    life_form = models.CharField(
        max_length=3,
        choices=LIFE_FORM_CHOICES,
        blank=True,
        verbose_name=_("Lebensform"),
    )
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, blank=True, verbose_name=_("Status")
    )
    # ----------------------------------------------------------------------------------
    other_features = models.CharField(
        max_length=200,
        blank=True,
        verbose_name=_("Weitere Merkmale"),
        help_text=_("Als eigenständigen Satz ausformulieren."),
    )

    class Meta:
        verbose_name = _("Pflanze")
        verbose_name_plural = _("Pflanzen")

    def taxonomy(self):
        tree_node = getattr(self, "tree_node")
        leaf = f"{tree_node.name} / {self.name}"

        return (
            leaf
            if tree_node.is_root_node()
            else f"{' / '.join(i.name for i in tree_node.get_ancestors())} / {leaf}"
        )

    taxonomy.short_description = _("Taxonomie")

    def name_without_markdown_symbols(self):
        return str(self)

    name_without_markdown_symbols.short_description = name.verbose_name

    def __str__(self):
        return self.name.replace("*", "").replace("_", "")


class Leaf(models.Model):
    plant = models.OneToOneField(
        Plant, on_delete=models.CASCADE, related_name="leaf", verbose_name=_("Pflanze")
    )
    # general --------------------------------------------------------------------------
    color = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Farbe"),
        help_text=_("Grammatikalisch anpassen."),
    )
    venation = models.CharField(
        max_length=3, choices=VENATION_CHOICES, blank=True, verbose_name=_("Nervatur")
    )
    division = models.CharField(
        max_length=3,
        choices=DIVISION_CHOICES,
        blank=True,
        verbose_name=_("Gliederung"),
    )
    succulence = models.CharField(
        max_length=3,
        choices=SUCCULENCE_CHOICES,
        blank=True,
        verbose_name=_("Dickfleischigkeit"),
    )
    texture = models.CharField(
        max_length=3,
        choices=TEXTURE_CHOICES,
        blank=True,
        verbose_name=_("Beschaffenheit"),
    )
    cross_section = models.CharField(
        max_length=3,
        choices=CROSS_SECTION_CHOICES,
        blank=True,
        verbose_name=_("Querschnitt"),
    )
    basal_leaf_rosette = models.CharField(
        max_length=1,
        choices=BASAL_LEAF_ROSETTE_CHOICES,
        blank=True,
        verbose_name=_("Grundblattrosette"),
    )
    # attachment -----------------------------------------------------------------------
    attachment = ArrayField(
        base_field=models.CharField(max_length=3, choices=ATTACHMENT_CHOICES),
        size=2,
        blank=True,
        default=list,
        verbose_name=_("Anheftung (an Sprossachse)"),
    )
    arrangement = models.CharField(
        max_length=3,
        choices=ARRANGMENT_CHOICES,
        blank=True,
        verbose_name=_("Anordnung (an Sprossachse)"),
    )
    # lamina_compound_leaf -------------------------------------------------------------
    compound_leaf_number = models.CharField(
        max_length=10, blank=True, verbose_name=_("Anzahl")
    )
    compound_leaf_shape = ArrayField(
        base_field=models.CharField(max_length=3, choices=COMPOUND_LEAF_SHAPE_CHOICES),
        size=2,
        blank=True,
        default=list,
        verbose_name=_("Gestalt"),
    )
    compound_leaf_incision_number = models.CharField(
        max_length=10, blank=True, verbose_name=_("Einschnittanzahl")
    )
    compound_leaf_incision_depth = ArrayField(
        base_field=models.CharField(
            max_length=3, choices=COMPOUND_LEAF_INCISION_DEPTH_CHOICES
        ),
        size=2,
        blank=True,
        default=list,
        verbose_name=_("Einschnitttiefe"),
    )
    leaflet_incision_number = models.CharField(
        max_length=10, blank=True, verbose_name=_("Einschnittanzahl (Blättchen)")
    )
    leaflet_incision_addition = models.CharField(
        max_length=100, blank=True, verbose_name=_("Einschnittzusatz (Blättchen)")
    )
    leaflet_incision_depth = ArrayField(
        base_field=models.CharField(
            max_length=3, choices=LEAFLET_INCISION_DEPTH_CHOICES
        ),
        size=2,
        blank=True,
        default=list,
        verbose_name=_("Einschnitttiefe (Blättchen)"),
    )
    # lamina_simple_leaf ---------------------------------------------------------------
    simple_leaf_number = models.CharField(
        max_length=10, blank=True, verbose_name=_("Anzahl")
    )
    simple_leaf_shape = ArrayField(
        base_field=models.CharField(max_length=3, choices=SIMPLE_LEAF_SHAPE_CHOICES),
        size=2,
        blank=True,
        default=list,
        verbose_name=_("Gestalt"),
    )
    simple_leaf_incision_number = models.CharField(
        max_length=10, blank=True, verbose_name=_("Einschnittanzahl")
    )
    simple_leaf_incision_depth = ArrayField(
        base_field=models.CharField(
            max_length=3,
            choices=SIMPLE_LEAF_INCISION_DEPTH_CHOICES,
            verbose_name=_("Einschnitttiefe (einf. Blatt)"),
        ),
        size=2,
        blank=True,
        default=list,
    )
    # lamina_general -------------------------------------------------------------------
    edge = ArrayField(
        base_field=models.CharField(
            max_length=3,
            choices=EDGE_CHOICES,
            verbose_name=_("Spreiten-/Blättchenrand"),
        ),
        size=2,
        blank=True,
        default=list,
    )
    surface = ArrayField(
        base_field=models.CharField(
            max_length=3, choices=SURFACE_CHOICES, verbose_name=_("Blattoberfläche")
        ),
        size=2,
        blank=True,
        default=list,
    )
    stipule_edge = ArrayField(
        base_field=models.CharField(
            max_length=3,
            choices=STIPULE_EDGE_CHOICES,
            verbose_name=_("Nebenblattrand"),
        ),
        size=2,
        blank=True,
        default=list,
    )
    base = models.CharField(
        max_length=3, choices=BASE_CHOICES, blank=True, verbose_name=_("Spreitengrund")
    )
    apex = models.CharField(
        max_length=3,
        choices=APEX_CHOICES,
        blank=True,
        verbose_name=_("Spreitenspitze"),
    )
    # miscellaneous --------------------------------------------------------------------
    special_features = models.CharField(
        max_length=200, blank=True, verbose_name=_("Besondere Merkmale")
    )
    sheath = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Blattscheide"),
        help_text='"Nicht vorhanden" eingeben, um hervorzuheben, dass kein ausgeprägtes Merkmal existiert.',
    )
    seed_leaf_number = models.IntegerField(
        choices=SEED_LEAF_NUMBER_CHOICES,
        blank=True,
        null=True,
        verbose_name=_("Keimblattanzahl"),
    )
    # ----------------------------------------------------------------------------------

    class Meta:
        verbose_name = _("Blatt")
        verbose_name_plural = _("Blätter")


class LeafPoales(models.Model):
    plant = models.OneToOneField(
        Plant,
        on_delete=models.CASCADE,
        related_name="leafpoales",
        verbose_name=_("Pflanze"),
    )
    # overview -------------------------------------------------------------------------
    length = models.CharField(max_length=20, blank=True, verbose_name=_("Länge"))
    width = models.CharField(
        max_length=50,
        blank=True,
        verbose_name=_("Breite"),
        help_text=_("Bsp. 2–4(–6) mm"),
    )
    color = models.CharField(
        max_length=50,
        blank=True,
        verbose_name=_("Farbe"),
        help_text=_("Grammatikalisch anpassen."),
    )
    shape = models.CharField(
        max_length=1,
        choices=LEAFPOALES_SHAPE_CHOICES,
        blank=True,
        verbose_name=_("Form"),
    )
    hairiness = ArrayField(
        base_field=models.CharField(max_length=3, choices=HAIRINESS_CHOICES),
        size=2,
        blank=True,
        default=list,
        verbose_name=_("Behaarung"),
    )
    cross_section = ArrayField(
        base_field=models.CharField(
            max_length=3, choices=LEAFPOALES_CROSS_SECTION_CHOICES
        ),
        size=2,
        blank=True,
        default=list,
        verbose_name=_("Querschnitt"),
    )
    alignment = models.CharField(
        max_length=3, blank=True, verbose_name=_("Ausrichtung")
    )
    attachment_point = models.CharField(
        max_length=1,
        choices=ATTACHMENT_POINT_CHOICES,
        blank=True,
        verbose_name=_("Ansatzstelle"),
    )
    # leaf_blade -----------------------------------------------------------------------
    blade_shape = models.CharField(
        max_length=3, choices=BLADE_SHAPE_CHOICES, blank=True, verbose_name=_("Form"),
    )
    blade_shape_feature = models.CharField(
        max_length=50, blank=True, verbose_name=_("Besonderheit (Form)")
    )
    blade_corrugation = ArrayField(
        base_field=models.CharField(max_length=3, choices=BLADE_CORRUGATION_CHOICES),
        size=2,
        blank=True,
        default=list,
        verbose_name=_("Riefung"),
    )
    blade_double_groove = models.CharField(
        max_length=1,
        choices=BLADE_DOUBLE_GROOVE,
        blank=True,
        verbose_name=_("Doppelrille"),
    )
    blade_shine = models.CharField(
        max_length=3, choices=BLADE_SHINE_CHOICES, blank=True, verbose_name=_("Glanz")
    )
    blade_keel = models.CharField(
        max_length=1, choices=BLADE_KEEL_CHOICES, blank=True, verbose_name=_("Kiel")
    )
    blade_edge = models.CharField(
        max_length=3, choices=BLADE_EDGE_CHOICES, blank=True, verbose_name=_("Rand"),
    )
    blade_bud_system = models.CharField(
        max_length=1,
        choices=BLADE_BUD_SYSTEM_CHOICES,
        blank=True,
        verbose_name=_("Knospenanlage"),
    )
    # leaf_base ------------------------------------------------------------------------
    base_edge = models.CharField(
        max_length=1, choices=BASE_EDGE_CHOICES, blank=True, verbose_name=_("Rand")
    )
    base_auricle = models.CharField(
        max_length=1,
        choices=BASE_AURICLE_CHOICES,
        blank=True,
        verbose_name=_("Öhrchen"),
    )
    base_auricle_feature = models.CharField(
        max_length=50, blank=True, verbose_name=_("Besonderheit (Öhrchen)")
    )
    # ligule ---------------------------------------------------------------------------
    ligule_length = models.CharField(
        max_length=3, choices=LIGULE_LENGTH_CHOICES, blank=True, verbose_name=_("Länge")
    )
    ligule_color = models.CharField(
        max_length=50,
        blank=True,
        verbose_name=_("Farbe"),
        help_text=_("Grammatikalisch anpassen."),
    )
    ligule_shape = models.CharField(
        max_length=3, choices=LIGULE_SHAPE_CHOICES, blank=True, verbose_name=_("Form")
    )
    ligule_consistency = models.CharField(
        max_length=3,
        choices=LIGULE_CONSISTENCY_CHOICES,
        blank=True,
        verbose_name=_("Konsistenz"),
    )
    ligule_features = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Besonderheiten"),
        help_text=_("Als eigenständigen Satz ausformulieren."),
    )
    # leaf_sheath ----------------------------------------------------------------------
    sheath_coloring = models.CharField(
        max_length=50,
        blank=True,
        verbose_name=_("Färbung"),
        help_text=_("Grammatikalisch anpassen."),
    )
    sheath_connation = models.CharField(
        max_length=3,
        choices=SHEATH_CONNATION_CHOICES,
        blank=True,
        verbose_name=_("Verwachsung"),
    )
    sheath_features = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Besonderheiten"),
        help_text=_("Als eigenständigen Satz ausformulieren."),
    )
    # ----------------------------------------------------------------------------------

    class Meta:
        verbose_name = _("Blatt (Poales)")
        verbose_name_plural = _("Blätter (Poales)")


class Blossom(models.Model):
    plant = models.OneToOneField(
        Plant,
        on_delete=models.CASCADE,
        related_name="blossom",
        verbose_name=_("Pflanze"),
    )
    # season ---------------------------------------------------------------------------
    season = ArrayField(
        base_field=models.IntegerField(blank=True, null=True),
        size=4,
        blank=True,
        default=list,
        verbose_name=_("Blütezeit"),
    )
    # inflorescence --------------------------------------------------------------------
    inflorescence_number = models.CharField(
        max_length=10, blank=True, verbose_name=_("Anzahl")
    )
    inflorescence_type = models.CharField(
        max_length=3,
        choices=INFLORESCENCE_TYPE_CHOICES,
        blank=True,
        verbose_name=_("Typ"),
    )
    inflorescence_blossom_number = models.CharField(
        max_length=10, blank=True, verbose_name=_("Blütenanzahl (pro Stand)")
    )
    # general --------------------------------------------------------------------------
    merosity = models.IntegerField(
        choices=MEROSITY_CHOICES, blank=True, null=True, verbose_name=_("Zähligkeit")
    )
    symmetry = models.CharField(
        max_length=1, choices=SYMMETRY_CHOICES, blank=True, verbose_name=_("Symmetrie")
    )
    perianth = models.CharField(
        max_length=3,
        choices=PERIANTH_CHOICES,
        blank=True,
        verbose_name=_("Blütenhülle"),
    )
    perianth_shape = models.CharField(
        max_length=2,
        choices=PERIANTH_SHAPE_CHOICES,
        blank=True,
        verbose_name=_("Blütenhüllenform (verwachsenblättrig)"),
    )
    bract_shape = ArrayField(
        base_field=models.CharField(max_length=3, choices=BRACT_SHAPE_CHOICES),
        size=2,
        blank=True,
        default=list,
        verbose_name=_("Tragblattgestalt"),
    )
    blossom_sex_distribution = models.CharField(
        max_length=1,
        choices=BLOSSOM_SEX_DISTRIBUTION_CHOICES,
        blank=True,
        verbose_name=_("Geschlechtigkeit"),
    )
    blossom_sex_distribution_addition = models.CharField(
        max_length=100, blank=True, verbose_name=_("Geschlechtigkeitzusatz")
    )
    plant_sex_distribution = models.CharField(
        max_length=1,
        choices=PLANT_SEX_DISTRIBUTION_CHOICES,
        blank=True,
        verbose_name=_("Häusigkeit"),
    )
    # diameter -------------------------------------------------------------------------
    diameter = models.CharField(
        max_length=20, blank=True, verbose_name=_("Durchmesser")
    )
    # sepal ----------------------------------------------------------------------------
    sepal_number = models.CharField(max_length=10, blank=True, verbose_name=_("Anzahl"))
    sepal_color_shape = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Farbe/Gestalt"),
        help_text=_("Grammatikalisch anpassen."),
    )
    sepal_connation_type = models.CharField(
        max_length=3, blank=True, verbose_name=_("Verwachsungstyp")
    )
    sepal_connation = models.CharField(
        max_length=1,
        choices=SEPAL_CONNATION_CHOICES,
        blank=True,
        verbose_name=_("Verwachsung"),
    )
    epicalyx = models.CharField(
        max_length=100, blank=True, verbose_name=_("Außenkelch")
    )
    # petal ----------------------------------------------------------------------------
    petal_number = models.CharField(max_length=10, blank=True, verbose_name=_("Anzahl"))
    petal_length = models.CharField(
        max_length=20, blank=True, verbose_name=_("Länge (Platte)")
    )
    petal_color_shape = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Farbe/Gestalt"),
        help_text=_("Grammatikalisch anpassen."),
    )
    petal_connation_type = models.CharField(
        max_length=3, blank=True, verbose_name=_("Verwachsungstyp")
    )
    petal_connation = models.CharField(
        max_length=1,
        choices=PETAL_CONNATION_CHOICES,
        blank=True,
        verbose_name=_("Verwachsung"),
    )
    nectary = models.CharField(
        max_length=100, blank=True, verbose_name=_("Nektarium/Honigdrüse")
    )
    # tepal ----------------------------------------------------------------------------
    tepal_number = models.CharField(max_length=10, blank=True, verbose_name=_("Anzahl"))
    tepal_color_shape = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Farbe/Gestalt"),
        help_text=_("Grammatikalisch anpassen."),
    )
    tepal_connation_type = models.CharField(
        max_length=3, blank=True, verbose_name=_("Verwachsungstyp")
    )
    tepal_connation = models.CharField(
        max_length=1,
        choices=TEPAL_CONNATION_CHOICES,
        blank=True,
        verbose_name=_("Verwachsung"),
    )
    # stamen ---------------------------------------------------------------------------
    stamen_number = models.CharField(
        max_length=10, blank=True, verbose_name=_("Anzahl")
    )
    stamen_length = models.CharField(max_length=20, blank=True, verbose_name=_("Länge"))
    stamen_color_shape = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Farbe/Gestalt"),
        help_text=_("Grammatikalisch anpassen."),
    )
    stamen_connation_type = models.CharField(
        max_length=1,
        choices=STAMEN_CONNATION_TYPE_CHOICES,
        blank=True,
        verbose_name=_("Verwachsungstyp"),
    )
    stamen_connation_type_addition = models.CharField(
        max_length=100, blank=True, verbose_name=_("Verwachsungstypzusatz")
    )
    # carpel ---------------------------------------------------------------------------
    carpel_number = models.CharField(
        max_length=10, blank=True, verbose_name=_("Anzahl")
    )
    carpel_connation_type = models.CharField(
        max_length=2,
        choices=CARPEL_CONNATION_TYPE_CHOICES,
        blank=True,
        verbose_name=_("Verwachsungstyp"),
    )
    ovary_number = models.CharField(
        max_length=10, blank=True, verbose_name=_("Fruchtknotenanzahl")
    )
    ovary_position = models.CharField(
        max_length=2,
        choices=OVARY_POSITION_CHOICES,
        blank=True,
        verbose_name=_("Fruchtknotenstellung"),
    )
    pistil_number = models.CharField(
        max_length=10, blank=True, verbose_name=_("Griffelanzahl")
    )
    pistil_position = models.CharField(
        max_length=3,
        choices=PISTIL_POSITION_CHOICES,
        blank=True,
        verbose_name=_("Griffelstellung"),
    )
    stigma_number = models.CharField(
        max_length=10, blank=True, verbose_name=_("Narbenanzahl (pro Griffel)")
    )
    stylopodium = models.CharField(
        max_length=100, blank=True, verbose_name=_("Griffelpolster")
    )
    # specifications -------------------------------------------------------------------
    specifications = models.TextField(
        max_length=600,
        blank=True,
        verbose_name=_("Spezifikationen"),
        help_text=_("Mit eigenständigem Satzbau ausformulieren."),
    )
    # ----------------------------------------------------------------------------------

    class Meta:
        verbose_name = _("Blüte")
        verbose_name_plural = _("Blüten")


class BlossomPoales(models.Model):
    plant = models.OneToOneField(
        Plant,
        on_delete=models.CASCADE,
        related_name="blossompoales",
        verbose_name=_("Pflanze"),
    )
    # season ---------------------------------------------------------------------------
    season = ArrayField(
        base_field=models.IntegerField(blank=True, null=True),
        size=4,
        blank=True,
        default=list,
        verbose_name=_("Blütezeit"),
    )
    # inflorescence --------------------------------------------------------------------
    inflorescence_blossom_number = models.CharField(
        max_length=20, blank=True, verbose_name=_("Blütenanzahl")
    )
    inflorescence_density = models.CharField(
        max_length=1,
        choices=INFLORESCENCE_DENSITY_CHOICES,
        blank=True,
        verbose_name=_("Dichte"),
    )
    inflorescence_position = models.CharField(
        max_length=1,
        choices=INFLORESCENCE_POSITION_CHOICES,
        blank=True,
        verbose_name=_("Stellung"),
    )
    inflorescence_type = models.CharField(
        max_length=1,
        choices=BP_INFLORESCENCE_TYPE_CHOICES,
        blank=True,
        verbose_name=_("Typ"),
    )
    inflorescence_features = models.CharField(
        max_length=50, blank=True, verbose_name=_("Besonderheiten")
    )
    inflorescence_bract_length = models.CharField(
        max_length=20, blank=True, verbose_name=_("Tragblattlänge")
    )
    inflorescence_bract_feature = models.CharField(
        max_length=50, blank=True, verbose_name=_("Besonderheit (Tragblatt)")
    )
    # blossom_perianth -----------------------------------------------------------------
    blossom_sex = models.CharField(
        max_length=1,
        choices=BLOSSOM_SEX_CHOICES,
        blank=True,
        verbose_name=_("Geschlecht"),
    )
    perianth = models.CharField(
        max_length=1,
        choices=BP_PERIANTH_CHOICES,
        blank=True,
        verbose_name=_("Blütenhülle"),
    )
    blossom_description = models.TextField(
        max_length=200,
        blank=True,
        verbose_name=_("Blüte (Beschreibung)"),
        help_text=_("Mit eigenständigem Satzbau ausformulieren."),
    )
    perianth_description = models.TextField(
        max_length=200,
        blank=True,
        verbose_name=_("Blütenhülle (Beschreibung)"),
        help_text=_("Mit eigenständigem Satzbau ausformulieren."),
    )
    # spikelet -------------------------------------------------------------------------
    spikelet_length = models.CharField(
        max_length=20, blank=True, verbose_name=_("Länge")
    )
    spikelet_shape = models.CharField(
        max_length=3,
        choices=SPIKELET_SHAPE_CHOICES,
        blank=True,
        verbose_name=_("Form"),
    )
    spikelet_attachment = models.CharField(
        max_length=3,
        choices=SPIKELET_ATTACHMENT_CHOICES,
        blank=True,
        verbose_name=_("Ansatz"),
    )
    spikelet_sex = models.CharField(
        max_length=1,
        choices=SPIKELET_SEX_CHOICES,
        blank=True,
        verbose_name=_("Geschlecht"),
    )
    spikelet_blossom_number = models.CharField(
        max_length=20, blank=True, verbose_name=_("Blütenanzahl")
    )
    spikelet_max_width = models.CharField(
        max_length=2,
        choices=SPIKELET_MAX_WIDTH_CHOICES,
        blank=True,
        verbose_name=_("Breitenmaxium"),
    )
    spikelet_rachilla = models.CharField(
        max_length=3,
        choices=SPIKELET_RACHILLA_CHOICES,
        blank=True,
        verbose_name=_("Achse"),
    )
    spikelet_stalk = models.CharField(
        max_length=3,
        choices=SPIKELET_STALK_CHOICES,
        blank=True,
        verbose_name=_("Stiel"),
    )
    spikelet_spindle = models.CharField(
        max_length=1,
        choices=SPIKELET_SPINDLE_CHOICES,
        blank=True,
        verbose_name=_("Spindel"),
    )
    spikelet_features = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Besonderheiten"),
        help_text=_("Als eigenständigen Satz ausformulieren."),
    )
    # husks ----------------------------------------------------------------------------
    husks_form = models.CharField(
        max_length=1, choices=HUSKS_FORM_CHOICES, blank=True, verbose_name=_("Form"),
    )
    husks_keel = models.CharField(
        max_length=1, choices=HUSKS_KEEL_CHOICES, blank=True, verbose_name=_("Kiel"),
    )
    husks_cross_section = ArrayField(
        base_field=models.CharField(max_length=1, choices=HUSKS_CROSS_SECTION_CHOICES),
        size=2,
        blank=True,
        default=list,
        verbose_name=_("Querschnitt"),
    )
    husks_description = models.TextField(
        max_length=400,
        blank=True,
        verbose_name=_("Beschreibung"),
        help_text=_("Mit eigenständigem Satzbau ausformulieren."),
    )
    # ----------------------------------------------------------------------------------

    class Meta:
        verbose_name = _("Blüte (Poales)")
        verbose_name_plural = _("Blüten (Poales)")


class Fruit(models.Model):
    plant = models.OneToOneField(
        Plant, on_delete=models.CASCADE, related_name="fruit", verbose_name=_("Pflanze")
    )
    # fruit ----------------------------------------------------------------------------
    fruit_color_shape = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Farbe/Gestalt"),
        help_text=_("Grammatikalisch anpassen."),
    )
    fruit_type = models.CharField(
        max_length=3, choices=FRUIT_TYPE_CHOICES, blank=True, verbose_name=_("Typ")
    )
    # ovule ----------------------------------------------------------------------------
    ovule_position = models.CharField(
        max_length=2,
        choices=OVULE_POSITION_CHOICES,
        blank=True,
        verbose_name=_("Lage"),
    )
    # seed -----------------------------------------------------------------------------
    seed_number = models.CharField(max_length=10, blank=True, verbose_name=_("Anzahl"))
    seed_color_shape = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Farbe/Gestalt"),
        help_text=_("Grammatikalisch anpassen."),
    )
    winging = models.CharField(
        max_length=100, blank=True, verbose_name=_("Beflügelung")
    )
    # ----------------------------------------------------------------------------------

    class Meta:
        verbose_name = _("Frucht")
        verbose_name_plural = _("Früchte")


class StemRoot(models.Model):
    plant = models.OneToOneField(
        Plant,
        on_delete=models.CASCADE,
        related_name="stemroot",
        verbose_name=_("Pflanze"),
    )
    # trunk_morphology -----------------------------------------------------------------
    trunk_features = models.TextField(
        max_length=200,
        blank=True,
        verbose_name=_("Stammmerkmale"),
        help_text=_("Mit eigenständigem Satzbau ausformulieren."),
    )
    # stem_morphology ------------------------------------------------------------------
    stem_growth_orientation = ArrayField(
        base_field=models.CharField(
            max_length=3, choices=STEM_GROWTH_ORIENTATION_CHOICES
        ),
        size=2,
        blank=True,
        default=list,
        verbose_name=_("Wuchsorientierung"),
    )
    stem_appearance = ArrayField(
        base_field=models.CharField(max_length=1, choices=STEM_APPEARANCE_CHOICES),
        size=2,
        blank=True,
        default=list,
        verbose_name=_("Erscheinung"),
    )
    stem_succulence = models.CharField(
        max_length=3,
        choices=SR_STEM_SUCCULENCE_CHOICES,
        blank=True,
        verbose_name=_("Dickfleischigkeit"),
    )
    stem_pith = models.CharField(
        max_length=1, choices=SR_STEM_PITH_CHOICES, blank=True, verbose_name=_("Mark")
    )
    stem_cross_section = ArrayField(
        base_field=models.CharField(
            max_length=3, choices=SR_STEM_CROSS_SECTION_CHOICES
        ),
        size=2,
        blank=True,
        default=list,
        verbose_name=_("Querschnitt"),
    )
    stem_surface = ArrayField(
        base_field=models.CharField(max_length=3, choices=SR_STEM_SURFACE_CHOICES),
        size=2,
        blank=True,
        default=list,
        verbose_name=_("Oberfläche"),
    )
    # outgrowths -----------------------------------------------------------------------
    creep_lay_shoots = models.BooleanField(
        choices=CREEP_LAY_SHOOTS_CHOICES,
        blank=True,
        null=True,
        verbose_name=_("Kriech- und Legetriebe"),
    )
    runners = models.BooleanField(
        choices=RUNNERS_CHOICES,
        blank=True,
        null=True,
        verbose_name=_("Ausläufer (oberirdisch)"),
    )
    # milky_sap ------------------------------------------------------------------------
    milky_sap = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Milchsaft"),
        help_text=_('Als eigenständigen Satz ausformulieren. Bsp. "Gelber Milchsaft."'),
    )
    # root_morphology ------------------------------------------------------------------
    root_organ_features = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Besonderheiten"),
        help_text="Besondere Ausprägungen der unterirdischen Organe.",
    )
    root_organs = models.CharField(
        max_length=3,
        choices=ROOT_ORGANS_CHOICES,
        blank=True,
        verbose_name=_("Organe (unterirdisch)"),
    )
    root_primary_root = models.CharField(
        max_length=3,
        choices=ROOT_PRIMARY_ROOT_CHOICES,
        blank=True,
        verbose_name=_("Primärwurzel"),
    )
    # ----------------------------------------------------------------------------------
    class Meta:
        verbose_name = _("Spross und Wurzel")
        verbose_name_plural = _("Sprosse und Wurzeln")


class StemRhizomePoales(models.Model):
    plant = models.OneToOneField(
        Plant,
        on_delete=models.CASCADE,
        related_name="stemrhizomepoales",
        verbose_name=_("Pflanze"),
    )
    # growth_form ----------------------------------------------------------------------
    tuft_stolon = models.CharField(
        max_length=3,
        choices=TUFT_STOLON_CHOICES,
        blank=True,
        verbose_name=_("Horst/Ausläufer"),
    )
    # stem -----------------------------------------------------------------------------
    stem_color = models.CharField(
        max_length=50,
        blank=True,
        verbose_name=_("Farbe"),
        help_text=_("Grammatikalisch anpassen."),
    )
    stem_hairiness = models.CharField(
        max_length=1,
        choices=STEM_HAIRINESS_CHOICES,
        blank=True,
        verbose_name=_("Behaarung"),
    )
    stem_cross_section = ArrayField(
        base_field=models.CharField(max_length=3, choices=STEM_CROSS_SECTION_CHOICES),
        size=2,
        blank=True,
        default=list,
        verbose_name=_("Querschnitt"),
    )
    stem_pith = models.CharField(
        max_length=1, choices=STEM_PITH_CHOICES, blank=True, verbose_name=_("Mark"),
    )
    stem_nodes = models.CharField(
        max_length=1, choices=STEM_NODES_CHOICES, blank=True, verbose_name=_("Knoten"),
    )
    stem_nodes_hairiness = models.CharField(
        max_length=1,
        choices=STEM_NODES_HAIRINESS_CHOICES,
        blank=True,
        verbose_name=_("Behaarung (Knoten)"),
    )
    stem_transverse_walls = models.CharField(
        max_length=1,
        choices=STEM_TRANSVERSE_WALLS_CHOICES,
        blank=True,
        verbose_name=_("Querwände"),
    )
    stem_surface = models.CharField(
        max_length=10, blank=True, verbose_name=_("Oberfläche"),
    )
    stem_features = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Besonderheiten"),
        help_text=_("Als eigenständigen Satz ausformulieren."),
    )
    # rhizome --------------------------------------------------------------------------
    rhizome_length = models.CharField(
        max_length=1,
        choices=RHIZOME_LENGTH_CHOICES,
        blank=True,
        verbose_name=_("Länge"),
    )
    rhizome_branching = models.CharField(
        max_length=1,
        choices=RHIZOME_BRANCHING_CHOICES,
        blank=True,
        verbose_name=_("Verzweigung"),
    )
    # ----------------------------------------------------------------------------------

    class Meta:
        verbose_name = _("Halm und Rhizom (Poales)")
        verbose_name_plural = _("Halme und Rhizome (Poales)")


class Indicators(models.Model):
    plant = models.OneToOneField(
        Plant,
        on_delete=models.CASCADE,
        related_name="indicators",
        verbose_name=_("Pflanze"),
    )
    not_specified = models.BooleanField(
        default=False,
        verbose_name=_("Keine Angabe"),
        help_text=_("Die Ausgabe aller Zeigerwerte wird unterdrückt."),
    )
    light = models.CharField(max_length=10, blank=True, verbose_name=_("Lichtzahl"))
    temperature = models.CharField(
        max_length=10, blank=True, verbose_name=_("Temperaturzahl")
    )
    humidity = models.CharField(
        max_length=10, blank=True, verbose_name=_("Feuchtezahl")
    )
    reaction = models.CharField(
        max_length=10, blank=True, verbose_name=_("Reaktionszahl")
    )
    nitrogen = models.CharField(
        max_length=10, blank=True, verbose_name=_("Stickstoffzahl")
    )
    key = ArrayField(
        base_field=models.CharField(max_length=3), default=list, editable=False
    )

    class Meta:
        verbose_name = _("Zeigerwerte")
        verbose_name_plural = _("Zeigerwerte")

    def get_key(self):
        return ", ".join(f"{dict(KEY_CHOICES).get(key)}" for key in self.key)

    get_key.short_description = _("Zeichenerklärung")


class InterestingFacts(models.Model):
    plant = models.OneToOneField(
        Plant,
        on_delete=models.CASCADE,
        related_name="interestingfacts",
        verbose_name=_("Pflanze"),
    )
    pollination = ArrayField(
        base_field=models.CharField(max_length=3, choices=POLLINATION_CHOICES),
        blank=True,
        default=list,
        verbose_name=_("Bestäubung"),
    )
    insects = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Insekten"),
        help_text=_("Zusatzangabe zur Insektenbestäubung"),
    )
    dispersal = ArrayField(
        base_field=models.CharField(max_length=3, choices=DISPERSAL_CHOICES),
        blank=True,
        default=list,
        verbose_name=_("Ausbreitung"),
    )
    detail_features = models.CharField(
        max_length=200,
        blank=True,
        verbose_name=_("Detailierte Merkmale"),
        help_text=_("Als eigenständigen Satz ausformulieren."),
    )
    usage = models.CharField(
        max_length=200,
        blank=True,
        verbose_name=_("Verwendung"),
        help_text=_("Als eigenständigen Satz ausformulieren. Markdown"),
    )
    trivia = models.TextField(
        max_length=600,
        blank=True,
        verbose_name=_("Trivia"),
        help_text=_("Mit eigenständigem Satzbau ausformulieren. Markdown"),
    )

    class Meta:
        verbose_name = _("Wissenswertes")
        verbose_name_plural = _("Wissenswertes")
