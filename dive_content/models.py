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
    short_description = models.TextField(
        default="", max_length=600, blank=True, verbose_name=_("Kurzbeschreibung")
    )
    name = models.CharField(max_length=100, verbose_name=_("Art"))
    trivial_name = models.CharField(max_length=100, verbose_name=_("Trivialname"))
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
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, blank=True, verbose_name=_("Status")
    )
    interaction = models.CharField(
        max_length=3,
        choices=INTERACTION_CHOICES,
        blank=True,
        verbose_name=_("Interaktionen"),
    )
    ground = ArrayField(
        base_field=models.CharField(
            max_length=3, choices=GROUND_CHOICES, verbose_name=_("Untergrund")
        ),
        size=2,
        blank=True,
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

    class Meta:
        verbose_name = _("Pflanze")
        verbose_name_plural = _("Pflanzen")

    def taxonomy(self):
        tree_node = getattr(self, "tree_node")
        leaf = "<i>{}</i> / <i>{}</i>".format(tree_node.name, self.name)

        if tree_node.is_root_node():
            output = leaf
        else:
            ancestors = " / ".join(obj.name for obj in tree_node.get_ancestors())
            output = ancestors + " / " + leaf

        return format_html(output)

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
        max_length=10, blank=True, verbose_name=_("Blattanzahl (zusg. Blätter)"),
    )
    blade_subdiv_shape = ArrayField(
        base_field=models.CharField(
            max_length=3,
            choices=BLADE_SUBDIV_SHAPE_CHOICES,
            verbose_name=_("Spreitengestalt (unterteiltes Blatt)"),
        ),
        size=2,
        blank=True,
        default=list,
    )
    incision_num = models.CharField(
        max_length=10, blank=True, verbose_name=_("Einschnittanzahl"),
    )
    incision_depth = ArrayField(
        base_field=models.CharField(
            max_length=3,
            choices=INCISION_DEPTH_CHOICES,
            verbose_name=_("Einschnitttiefe"),
        ),
        size=2,
        blank=True,
        default=list,
    )
    leaflet_incision_num = models.CharField(
        max_length=10, blank=True, verbose_name=_("Einschnittanzahl (Blättchen)"),
    )
    leaflet_incision_add = models.CharField(
        max_length=100, blank=True, verbose_name=_("Einschnittzusatz (Blättchen)"),
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
        max_length=10, blank=True, verbose_name=_("Blattanzahl (einf. Blätter)"),
    )
    blade_undiv_shape = ArrayField(
        base_field=models.CharField(
            max_length=3,
            choices=BLADE_UNDIV_SHAPE_CHOICES,
            verbose_name=_("Spreitengestalt (ungeteiltes Blatt)"),
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
            max_length=3, choices=SURFACE_CHOICES, verbose_name=_("Blattoberfläche"),
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
        max_length=200,
        blank=True,
        verbose_name=_("Besondere Merkmale"),
        help_text='"Nicht vorhanden" eingeben, um hervorzuheben, dass kein ausgeprägtes Merkmal existiert.',
    )
    sheath = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Blattscheide"),
        help_text='"Nicht vorhanden" eingeben, um hervorzuheben, dass kein ausgeprägtes Merkmal existiert.',
    )
    seed_leaf_num = models.IntegerField(
        choices=((1, 1), (2, 2)),
        blank=True,
        null=True,
        verbose_name=_("Keimblattanzahl"),
    )

    class Meta:
        verbose_name = _("Blatt")
        verbose_name_plural = _("Blätter")


class Blossom(models.Model):
    season = models.CharField(
        max_length=200,
        blank=True,
        verbose_name=_("Blütezeit"),
        help_text="Bsp. (Januar) Februar bis März",
    )
    type = models.CharField(
        max_length=3,
        choices=BL_TYPE_CHOICES,
        blank=True,
        verbose_name=_("Blütenstandsform"),
    )
    bl_cnt = models.CharField(
        max_length=100, blank=True, verbose_name=_("Blüten pro Blütenstand")
    )
    sym = models.CharField(
        max_length=1, choices=SYM_CHOICES, blank=True, verbose_name=_("Symmetrie")
    )
    parting = models.CharField(
        max_length=3,
        choices=PART_CHOICES,
        blank=True,
        verbose_name=_("Tragblattspreite"),
    )
    cnt = models.IntegerField(
        choices=((3, 3), (4, 4), (5, 5)),
        blank=True,
        null=True,
        verbose_name=_("Zähligkeit"),
    )
    hull = models.CharField(
        max_length=3, choices=HULL_CHOICES, blank=True, verbose_name=_("Blütenhülle")
    )

    chalice = models.CharField(
        max_length=1,
        choices=(("v", _("verwachsen")), ("u", _("unverwachsen"))),
        blank=True,
        verbose_name=_("Kelchblätter"),
    )
    ch_type = models.CharField(
        max_length=3,
        choices=CH_TYPE_CHOICES,
        blank=True,
        verbose_name=_("Verwachsungstyp"),
    )

    crown_color = models.CharField(
        max_length=100, blank=True, verbose_name=_("Kronblattfarbe")
    )
    crown_ver = models.CharField(
        max_length=1,
        choices=CROWN_VER_CHOICES,
        blank=True,
        verbose_name=_("Verwachsung der Kronblätter"),
    )
    crown_plate = models.CharField(
        max_length=100, blank=True, verbose_name=_("Kronblatt Platte")
    )
    crown_lower = models.CharField(
        max_length=3,
        choices=CH_TYPE_CHOICES,
        blank=True,
        verbose_name=_("Kronblatt Unterlippe"),
    )
    crown_out = models.CharField(
        max_length=100, blank=True, verbose_name=_("Ausstülpung der Unterlippe")
    )

    dust_cnt = models.CharField(
        max_length=100, blank=True, verbose_name=_("Staubblatt Anzahl")
    )
    dust_len = models.CharField(
        max_length=100, blank=True, verbose_name=_("Staubblatt Länge")
    )
    dust_color = models.CharField(
        max_length=100, blank=True, verbose_name=_("Staubbeutel Farbe")
    )
    dust_pipe = models.CharField(
        max_length=100, blank=True, verbose_name=_("Staubfadenröhre")
    )

    fruit_cnt = models.CharField(
        max_length=100, blank=True, verbose_name=_("Fruchtknoten Anzahl")
    )
    fruit_stand = models.CharField(
        max_length=2,
        choices=STAND_TYPE_CHOICES,
        blank=True,
        verbose_name=_("Ständigkeit des Fruchtknotens"),
    )
    fruit_build = models.CharField(
        max_length=2,
        choices=BUILD_CHOICES,
        blank=True,
        verbose_name=_("Bau des Gynoeceums"),
    )
    fruit_scar = models.CharField(
        max_length=100, blank=True, verbose_name=_("Narben pro Griffel")
    )
    griffel_stand = models.CharField(
        max_length=2,
        choices=GRIFFEL_CHOICES,
        blank=True,
        verbose_name=_("Ständigkeit des Griffels"),
    )
    griffel_sub = models.CharField(
        max_length=3,
        choices=GRIFFEL_SUB_CHOICES,
        blank=True,
        verbose_name=_("Ständigkeit des Griffels ist sub-"),
    )

    spec_sporn = models.CharField(
        max_length=2, choices=SPEC_SPORN_CHOICES, blank=True, verbose_name=_("Sporn")
    )
    spec_hon = models.CharField(
        max_length=100, blank=True, verbose_name=_("Honigdrüsen / Nektarien")
    )
    sec_out = models.CharField(max_length=100, blank=True, verbose_name=_("Außenkelch"))
    spec_pol = models.CharField(
        max_length=100, blank=True, verbose_name=_("Griffelpolster")
    )
    spec_pipe = models.CharField(max_length=100, blank=True, verbose_name=_("Schlauch"))

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

    plant = models.OneToOneField(
        Plant,
        on_delete=models.CASCADE,
        related_name="blossom",
        verbose_name=_("Pflanze"),
    )

    class Meta:
        verbose_name = _("Blüte")
        verbose_name_plural = _("Blüten")


class Fruit(models.Model):
    plant = models.OneToOneField(
        Plant, on_delete=models.CASCADE, related_name="fruit", verbose_name=_("Pflanze")
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
    seed_form = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Samenform"),
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


class Sprout(models.Model):
    appear = models.CharField(
        max_length=1,
        choices=(("k", _("krautig")), ("h", _("holzig"))),
        blank=True,
        verbose_name=_("Erscheinung"),
    )
    pos = models.CharField(
        max_length=3,
        choices=POSITION_CHOICES,
        blank=True,
        verbose_name=_("Wuchsorientierung"),
    )
    thick_flesh = models.CharField(
        null=True,
        blank=True,
        max_length=3,
        choices=YES_NO_CHOICES,
        verbose_name=_("Dickfleischig"),
    )
    milk = models.CharField(
        max_length=3, null=True, blank=True, verbose_name=_("Milchsaft")
    )
    leafly = models.CharField(
        max_length=3,
        choices=(("nur", _("Nur am Grund")), ("auc", _("Auch über Grund"))),
        blank=True,
        verbose_name=_("Beblätterung"),
    )
    diam = models.CharField(
        max_length=3, choices=SP_DIAM_CHOICES, blank=True, verbose_name=_("Querschnitt")
    )
    sur_texture = models.CharField(
        max_length=3,
        choices=SUR_TEXTURE_CHOICES,
        blank=True,
        verbose_name=_("Sprossoberfläche"),
    )
    primary_root = models.CharField(
        max_length=3, choices=ROOT_CHOICES, blank=True, verbose_name=_("Primärwurzel")
    )
    blade = models.CharField(max_length=200, blank=True, verbose_name=_("Halm"))
    cluster = models.CharField(max_length=200, blank=True, verbose_name=_("Horst"))

    plant = models.OneToOneField(
        Plant,
        on_delete=models.CASCADE,
        related_name="sprout",
        verbose_name=_("Pflanze"),
    )

    class Meta:
        verbose_name = _("Spross")
        verbose_name_plural = _("Spross")


class ZeigerNumber(models.Model):
    light_number = models.CharField(
        max_length=100,
        choices=LIGHT_CHOICES,
        blank=True,
        null=True,
        verbose_name=_("Lichtzahl"),
    )
    light_extra = models.CharField(
        max_length=100, choices=ZEIGER_EXTRA, blank=True, null=True
    )
    temp_number = models.CharField(
        max_length=100,
        choices=TEMP_CHOICES,
        blank=True,
        null=True,
        verbose_name=_("Temperaturzahl"),
    )
    temp_extra = models.CharField(
        max_length=100, choices=ZEIGER_EXTRA, blank=True, null=True
    )
    humid_number = models.CharField(
        max_length=100,
        choices=HUMID_CHOICES,
        blank=True,
        null=True,
        verbose_name=_("Feuchtezahl"),
    )
    humid_extra = models.CharField(
        max_length=100, choices=ZEIGER_EXTRA, blank=True, null=True
    )
    react_number = models.CharField(
        max_length=100,
        choices=REACT_CHOICES,
        blank=True,
        null=True,
        verbose_name=_("Reaktionszahl"),
    )
    react_extra = models.CharField(
        max_length=100, choices=ZEIGER_EXTRA, blank=True, null=True
    )
    nutri_number = models.CharField(
        max_length=100,
        choices=NUTRIENT_CHOICES,
        blank=True,
        null=True,
        verbose_name=_("Stickstoff/Nährstoffzahl"),
    )
    nutri_extra = models.CharField(
        max_length=100, choices=ZEIGER_EXTRA, blank=True, null=True
    )

    plant = models.OneToOneField(
        Plant,
        on_delete=models.CASCADE,
        related_name="zeigernumber",
        verbose_name=_("Pflanze"),
    )

    class Meta:
        verbose_name = _("Zeigerzahl")
        verbose_name_plural = _("Zeigerzahlen")
