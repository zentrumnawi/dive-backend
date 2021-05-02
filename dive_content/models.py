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
    ARTICLE_CHOICES = (("der", _("Der")), ("die", _("Die")), ("das", _("Das")))
    HABITAT_CHOICES = (
        ("sch", _("Schlammfluren")),
        ("roe", _("Röhrichte")),
        ("sae", _("Säume")),
        ("sta", _("Staudenfluren")),
        ("gru", _("Grünland und Zwergstrauchheiden")),
        ("rud", _("Ruderalvegetation")),
        ("aec", _("Äcker")),
        ("wei", _("Weinberge")),
        ("int", _("Intensivgrünland")),
        ("par", _("Parks")),
        ("gae", _("Gärten")),
        ("tri", _("Trittpflanzengesellschaften")),
        ("fel", _("Felsbiotope")),
        ("aue", _("Auenwälder")),
        ("geb", _("Gebüsche")),
        ("ger", _("Geröll")),
        ("ext", _("Extensivgrünland oder natürlicher Rasen")),
        ("wae", _("Wälder")),
        ("ufe", _("Ufer")),
    )
    STATUS_CHOICES = (
        ("e", _("einheimisch")),
        ("a", _("Archaeophyt")),
        ("n", _("Neophyt")),
    )
    INTERACTION_CHOICES = (
        ("par", _("parasitisch")),
        ("nip", _("nicht parasitisch")),
        ("obl", _("obligate Mykorrhiza")),
        ("fak", _("fakultative Mykorrhiza")),
    )
    GROUND_CHOICES = (
        ("leh", _("lehmig")),
        ("tor", _("torfig")),
        ("san", _("sandig")),
        ("ste", _("steinig/felsig")),
    )
    LIFE_FORM_CHOICES = (
        ("pha", _("Phanerophyt")),
        ("cha", _("Chamaephyt")),
        ("hem", _("Hemikryptophyt")),
        ("kry", _("Kryptophyt")),
        ("the", _("Therophyt")),
    )
    GROWTH_FORM_CHOICES = (
        ("bau", _("Baum")),
        ("str", _("Strauch")),
        ("stb", _("Strauchbaum")),
        ("zwe", _("Zwergstrauch")),
        ("lia", _("Liane")),
        ("kle", _("Kletterpflanze")),
        ("hal", _("Halbstrauch")),
        ("spa", _("Spalierstrauch")),
        ("krc", _("krautiger Chemaephyt")),
        ("geo", _("Geophyt")),
        ("hel", _("Helophyt (Sumpfpflanze)")),
        ("hyd", _("Hydrophyt (Wasserpflanze)")),
        ("tau", _("Tauchpflanze")),
        ("sch", _("Schwimmpflanze")),
    )
    DISPERSAL_CHOICES = (
        ("sa", _("Samenpflanze")),
        ("sp", _("Sporenpflanze")),
    )

    BaseProfile._meta.get_field("tree_node").verbose_name = _("Steckbrief-Ebene")
    name = models.CharField(max_length=100, verbose_name=_("Art"))
    article = models.CharField(
        max_length=3, choices=ARTICLE_CHOICES, blank=True, verbose_name=_("Artikel")
    )
    trivial_name = models.CharField(max_length=100, verbose_name=_("Trivialname"))
    short_description = models.TextField(
        default="", max_length=600, blank=True, verbose_name=_("Kurzbeschreibung")
    )
    alt_trivial_name = models.CharField(
        default="",
        max_length=500,
        blank=True,
        verbose_name=_("Liste alternativer Trivialnamen"),
    )
    habitat = ArrayField(
        base_field=models.CharField(
            max_length=3, choices=HABITAT_CHOICES, verbose_name=_("Habitat")
        ),
        blank=True,
    )
    ground = ArrayField(
        base_field=models.CharField(
            max_length=3, choices=GROUND_CHOICES, verbose_name=_("Untergrund")
        ),
        size=2,
        blank=True,
    )
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, blank=True, verbose_name=_("Status")
    )
    interaction = models.CharField(
        max_length=3,
        choices=INTERACTION_CHOICES,
        blank=True,
        verbose_name=_("Interaktionen"),
    )
    life_form = models.CharField(
        max_length=3,
        choices=LIFE_FORM_CHOICES,
        blank=True,
        verbose_name=_("Lebensform"),
    )
    growth_form = models.CharField(
        max_length=3,
        choices=GROWTH_FORM_CHOICES,
        blank=True,
        verbose_name=_("Wuchsform"),
    )
    growth_height = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Wuchshöhe"),
        help_text="Bsp. 10-15 cm",
    )
    dispersal = models.CharField(
        max_length=2,
        choices=DISPERSAL_CHOICES,
        blank=True,
        verbose_name=_("Ausbreitungsform"),
    )
    other_features = models.CharField(
        max_length=200,
        blank=True,
        verbose_name=_("Weitere Merkmale"),
        help_text="Bsp. Geruch",
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

    def get_ground_output(self):
        if self.ground:
            output = " bis ".join(
                str(dict(self.GROUND_CHOICES).get(item)) for item in self.ground
            )
        else:
            output = ""

        return output

    get_ground_output.short_description = _("Untergrund (Ausgabe)")

    def __str__(self):
        return self.name


class Leaf(models.Model):
    plant = models.OneToOneField(
        Plant, on_delete=models.CASCADE, related_name="leaf", verbose_name=_("Pflanze")
    )
    color = models.CharField(max_length=100, blank=True, verbose_name=_("Blattfarbe"))
    veins = models.CharField(
        max_length=3, choices=VEINS_CHOICES, blank=True, verbose_name=_("Blattnerven")
    )
    division = models.CharField(
        max_length=3,
        choices=DIVISION_CHOICES,
        blank=True,
        verbose_name=_("Spreitengliederung"),
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
    attachment = ArrayField(
        base_field=models.CharField(
            max_length=3,
            choices=ATTACHMENT_CHOICES,
            verbose_name=_("Anheftung (an Sprossachse)"),
        ),
        size=2,
        blank=True,
        default=list,
    )
    arrangement = models.CharField(
        max_length=3,
        choices=ARRANGMENT_CHOICES,
        blank=True,
        verbose_name=_("Anordnung (an Sprossachse)"),
    )
    rosette = models.CharField(
        max_length=3,
        choices=ROSETTE_CHOICES,
        blank=True,
        verbose_name=_("Grundblattrosette"),
    )
    leaf_comp_num = models.CharField(
        max_length=10, blank=True, verbose_name=_("Blattanzahl (zusg. Blatt)")
    )
    leaf_comp_blade_shape = ArrayField(
        base_field=models.CharField(
            max_length=3,
            choices=LEAF_COMP_BLADE_SHAPE_CHOICES,
            verbose_name=_("Spreitengestalt (zusg. Blatt)"),
        ),
        size=2,
        blank=True,
        default=list,
    )
    leaf_comp_incision_num = models.CharField(
        max_length=10, blank=True, verbose_name=_("Einschnittanzahl (zusg. Blatt)")
    )
    leaf_comp_incision_depth = ArrayField(
        base_field=models.CharField(
            max_length=3,
            choices=LEAF_COMP_INCISION_DEPTH_CHOICES,
            verbose_name=_("Einschnitttiefe (zusg. Blatt)"),
        ),
        size=2,
        blank=True,
        default=list,
    )
    leaflet_incision_num = models.CharField(
        max_length=10, blank=True, verbose_name=_("Einschnittanzahl (Blättchen)")
    )
    leaflet_incision_add = models.CharField(
        max_length=100, blank=True, verbose_name=_("Einschnittzusatz (Blättchen)")
    )
    leaflet_incision_depth = ArrayField(
        base_field=models.CharField(
            max_length=3,
            choices=LEAFLET_INCISION_DEPTH_CHOICES,
            verbose_name=_("Einschnitttiefe (Blättchen)"),
        ),
        size=2,
        blank=True,
        default=list,
    )
    leaf_simple_num = models.CharField(
        max_length=10, blank=True, verbose_name=_("Blattanzahl (einf. Blatt)")
    )
    leaf_simple_blade_shape = ArrayField(
        base_field=models.CharField(
            max_length=3,
            choices=LEAF_SIMPLE_BLADE_SHAPE_CHOICES,
            verbose_name=_("Spreitengestalt (einf. Blatt)"),
        ),
        size=2,
        blank=True,
        default=list,
    )
    leaf_simple_incision_num = models.CharField(
        max_length=10, blank=True, verbose_name=_("Einschnittanzahl (einf. Blatt)")
    )
    leaf_simple_incision_depth = ArrayField(
        base_field=models.CharField(
            max_length=3,
            choices=LEAF_SIMPLE_INCISION_DEPTH_CHOICES,
            verbose_name=_("Einschnitttiefe (einf. Blatt)"),
        ),
        size=2,
        blank=True,
        default=list,
    )
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
    special_features = models.CharField(
        max_length=200, blank=True, verbose_name=_("Besondere Merkmale")
    )
    sheath = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Blattscheide"),
        help_text='"Nicht vorhanden" eingeben, um hervorzuheben, dass kein ausgeprägtes Merkmal existiert.',
    )
    seed_leaf_num = models.IntegerField(
        choices=SEED_LEAF_NUM_CHOICES,
        blank=True,
        null=True,
        verbose_name=_("Keimblattanzahl"),
    )

    class Meta:
        verbose_name = _("Blatt")
        verbose_name_plural = _("Blätter")


class Blossom(models.Model):
    plant = models.OneToOneField(
        Plant,
        on_delete=models.CASCADE,
        related_name="blossom",
        verbose_name=_("Pflanze"),
    )
    season = ArrayField(
        base_field=models.IntegerField(
            blank=True, null=True, verbose_name=_("Blütezeit")
        ),
        size=4,
        blank=True,
        default=list,
    )
    inflorescence_num = models.CharField(
        max_length=10, blank=True, verbose_name=_("Blütenstandsanzahl")
    )
    inflorescence_type = models.CharField(
        max_length=3,
        choices=INFLORESCENCE_TYPE_CHOICES,
        blank=True,
        verbose_name=_("Blütenstandstyp"),
    )
    blossom_num = models.CharField(
        max_length=10, blank=True, verbose_name=_("Blütenanzahl (pro Stand)")
    )
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
    perianth_form = models.CharField(
        max_length=2,
        choices=PERIANTH_FORM_CHOICES,
        blank=True,
        verbose_name=_("Blütenhüllenform (verwachsenblättrig)"),
    )
    bract_blade = ArrayField(
        base_field=models.CharField(
            max_length=3,
            choices=BRACT_BLADE_CHOICES,
            verbose_name=_("Tragblattspreite"),
        ),
        size=2,
        blank=True,
        default=list,
    )
    diameter = models.CharField(
        max_length=10, blank=True, verbose_name=_("Durchmesser")
    )
    sepal_num = models.CharField(
        max_length=10, blank=True, verbose_name=_("Kelchblattanzahl")
    )
    sepal_color_form = models.CharField(
        max_length=100, blank=True, verbose_name=_("Farbe/Gestalt (Kelchblatt)")
    )
    sepal_connation_type = models.CharField(
        max_length=3, blank=True, verbose_name=_("Verwachsungstyp (Kelchblatt)")
    )
    sepal_connation = models.CharField(
        max_length=1,
        choices=SEPAL_CONNATION_CHOICES,
        blank=True,
        verbose_name=_("Verwachsung (Kelchblatt)"),
    )
    epicalyx = models.CharField(
        max_length=100, blank=True, verbose_name=_("Außenkelch")
    )
    petal_num = models.CharField(
        max_length=10, blank=True, verbose_name=_("Kronblattanzahl")
    )
    petal_len = models.CharField(
        max_length=10, blank=True, verbose_name=_("Kronblattlänge (Platte)")
    )
    petal_color_form = models.CharField(
        max_length=100, blank=True, verbose_name=_("Farbe/Gestalt (Kronblatt)")
    )
    petal_connation_type = models.CharField(
        max_length=3, blank=True, verbose_name=_("Verwachsungstyp (Kronblatt)")
    )
    petal_connation = models.CharField(
        max_length=1,
        choices=PETAL_CONNATION_CHOICES,
        blank=True,
        verbose_name=_("Verwachsung (Kronblatt)"),
    )
    nectary = models.CharField(
        max_length=100, blank=True, verbose_name=_("Nektarium/Honigdrüse")
    )
    stamen_num = models.CharField(
        max_length=10, blank=True, verbose_name=_("Staubblattanzahl")
    )
    stamen_len = models.CharField(
        max_length=10, blank=True, verbose_name=_("Staubblattlänge")
    )
    stamen_color_form = models.CharField(
        max_length=100, blank=True, verbose_name=_("Farbe/Gestalt (Staubblatt)")
    )
    stamen_connation_type = models.CharField(
        max_length=1,
        choices=STAMEN_CONNATION_TYPE_CHOICES,
        blank=True,
        verbose_name=_("Verwachsungstyp (Staubblatt)"),
    )
    stamen_connation_type_add = models.CharField(
        max_length=100, blank=True, verbose_name=_("Verwachsungstypzusatz")
    )
    carpel_num = models.CharField(
        max_length=10, blank=True, verbose_name=_("Fruchtblattanzahl")
    )
    carpel_connation_type = models.CharField(
        max_length=2,
        choices=CARPEL_CONNATION_TYPE_CHOICES,
        blank=True,
        verbose_name=_("Verwachsungstyp (Fruchtblatt)"),
    )
    ovary_pos = models.CharField(
        max_length=2,
        choices=OVARY_POS_CHOICES,
        blank=True,
        verbose_name=_("Fruchtknotenstellung"),
    )
    pistil_pos = models.CharField(
        max_length=3,
        choices=PISTIL_POS_CHOICES,
        blank=True,
        verbose_name=_("Griffelstellung"),
    )
    stigma_num = models.CharField(
        max_length=10, blank=True, verbose_name=_("Narbenanzahl (pro Griffel)")
    )
    stylopodium = models.CharField(
        max_length=100, blank=True, verbose_name=_("Griffelpolster")
    )
    # -------------------------------- TO BE MODIFIED -------------------------------- #
    grann_top = models.CharField(
        max_length=2,
        choices=GRANN_TOP_CHOICES,
        blank=True,
        verbose_name=_("Granne der Deckspelze"),
    )
    grann_form = models.CharField(
        max_length=2,
        choices=GRANN_FORM_CHOICES,
        blank=True,
        verbose_name=_("Form der Granne"),
    )
    cons_top = models.CharField(
        max_length=100, blank=True, verbose_name=_("Konsistenz der Deckspelze")
    )
    gull_spel = models.CharField(
        max_length=100, blank=True, verbose_name=_("Hüllspelzen")
    )
    blos = models.CharField(
        max_length=100, blank=True, verbose_name=_("Blütigkeit des Ährchens")
    )
    straw_ground = models.CharField(
        max_length=2,
        choices=GROUND_CHOICES,
        blank=True,
        verbose_name=_("Ansatz an Halm"),
    )
    order = models.CharField(
        max_length=100, blank=True, verbose_name=_("Ährchen pro Ähre")
    )
    aer_per_aer = models.CharField(
        max_length=100, blank=True, verbose_name=_("Anordnung der Ährchen")
    )
    aer_per_ab = models.CharField(
        max_length=100, blank=True, verbose_name=_("Ährchen pro Absatz der Ährenachse")
    )
    # -------------------------------------------------------------------------------- #
    class Meta:
        verbose_name = _("Blüte")
        verbose_name_plural = _("Blüten")


class Fruit(models.Model):
    plant = models.OneToOneField(
        Plant, on_delete=models.CASCADE, related_name="fruit", verbose_name=_("Pflanze")
    )
    fruit_form = models.CharField(
        max_length=100, blank=True, verbose_name=_("Fruchtform")
    )
    fruit_type = models.CharField(
        max_length=3,
        choices=FRUIT_TYPE_CHOICES,
        blank=True,
        verbose_name=_("Fruchttyp"),
    )
    ovule_pos = models.CharField(
        max_length=2,
        choices=OVULE_POS_CHOICES,
        blank=True,
        verbose_name=_("Samenanlage (Lage)"),
    )
    seed_num = models.CharField(
        max_length=10, blank=True, verbose_name=_("Samenanzahl")
    )
    seed_color_form = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Farbe/Form (Samen)"),
        help_text="Alles ausschreiben.",
    )
    winging = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Beflügelung"),
        help_text="Alles ausschreiben.",
    )
    winging_feature = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Besonderheit (Beflügelung)"),
        help_text="Alles ausschreiben.",
    )

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
    orientation = ArrayField(
        base_field=models.CharField(
            max_length=3,
            choices=ORIENTATION_CHOICES,
            verbose_name=_("Wuchsorientierung"),
        ),
        size=2,
        blank=True,
        default=list,
    )
    appearance = ArrayField(
        base_field=models.CharField(
            max_length=1, choices=APPEARANCE_CHOICES, verbose_name=_("Erscheinung"),
        ),
        size=2,
        blank=True,
        default=list,
    )
    succulence = models.CharField(
        max_length=3,
        choices=SUCCULENCE_CHOICES,
        blank=True,
        verbose_name=_("Dickfleischigkeit"),
    )
    pith = models.CharField(
        max_length=1, choices=PITH_CHOICES, blank=True, verbose_name=_("Mark")
    )
    cross_section = ArrayField(
        base_field=models.CharField(
            max_length=3,
            choices=SR_CROSS_SECTION_CHOICES,
            verbose_name=_("Querschnitt"),
        ),
        size=2,
        blank=True,
        default=list,
    )
    surface = ArrayField(
        base_field=models.CharField(
            max_length=3, choices=SURFACE_CHOICES, verbose_name=_("Sprossoberfläche")
        ),
        size=2,
        blank=True,
        default=list,
    )
    creep_lay_shoots = models.CharField(
        max_length=3,
        choices=CREEP_LAY_SHOOTS_CHOICES,
        blank=True,
        verbose_name=_("Kriech- und Legetriebe"),
    )
    runners = models.CharField(
        max_length=3,
        choices=RUNNERS_CHOICES,
        blank=True,
        verbose_name=_("Ausläufer (oberirdisch)"),
    )
    bracts = models.CharField(
        max_length=3,
        choices=BRACTS_CHOICES,
        blank=True,
        verbose_name=_("Beblätterung"),
    )
    milky_sap = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Milchsaft"),
        help_text="Bsp. kein Milchsaft, gelber Milchsaft, etc.",
    )
    organ_features = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Besonderheiten"),
        help_text="Besondere Ausprägungen der unterirdischen Organe.",
    )
    organs = models.CharField(
        max_length=3,
        choices=ORGANS_CHOICES,
        blank=True,
        verbose_name=_("Organe (unterirdisch)"),
    )
    primary_root = models.CharField(
        max_length=3,
        choices=PRIMARY_ROOT_CHOICES,
        blank=True,
        verbose_name=_("Primärwurzel"),
    )

    class Meta:
        verbose_name = _("Spross und Wurzel")
        verbose_name_plural = _("Sprosse und Wurzeln")


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
        max_length=10, blank=True, verbose_name=_("Temperaturzahl"),
    )
    humidity = models.CharField(
        max_length=10, blank=True, verbose_name=_("Feuchtezahl"),
    )
    reaction = models.CharField(
        max_length=10, blank=True, verbose_name=_("Reaktionszahl"),
    )
    nitrogen = models.CharField(
        max_length=10, blank=True, verbose_name=_("Stickstoffzahl"),
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
