from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import ugettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey

from .choices import *

# Custom Models, representing the actual data of a profile, implement here.
# At least one model needs to have a ForeignKey field to the TreeNode model
# with related_name="profiles". If not, the profiles endpoint will throw an
# error.


class Plant(models.Model):

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
        ("rei", _("nährstoffreich")),
        ("arm", _("nährstoffarm")),
        ("leh", _("lehmig")),
        ("tor", _("torfig")),
        ("san", _("sandig")),
        ("ste", _("steinig/felsig")),
    )
    ROOT_CHOICES = (
        ("erh", _("erhalten")),
        ("ers", _("ersetzt durch sprossbürtige Wurzeln")),
    )

    name = models.CharField(max_length=100, verbose_name=_("Art"))
    trivial_name = models.CharField(max_length=100, verbose_name=_("Trivialname"))
    habitat = ArrayField(
        base_field=models.CharField(max_length=3, choices=HABITAT_CHOICES),
        blank=True,
        verbose_name=_("Lebensraum"),
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
        base_field=models.CharField(max_length=3, choices=GROUND_CHOICES),
        blank=True,
        verbose_name=_("Untergrund"),
    )
    bloom = models.CharField(max_length=200, verbose_name=_("Blütezeit"))

    prime_root = models.CharField(
        max_length=3, choices=ROOT_CHOICES, blank=True, verbose_name=_("Primärwurzel")
    )
    nodule = models.BooleanField(verbose_name=_("Wurzelknollen"))

    systematics = models.ForeignKey(
        "TreeNode",
        related_name="profiles",
        on_delete=models.DO_NOTHING,
        null=True,
        verbose_name=_("Steckbrief-Ebene"),
    )


class Leaf(models.Model):

    nerves = models.CharField(
        max_length=3, choices=NERV_CHOICES, blank=True, verbose_name=_("Blattnerven")
    )
    cnt_germ = models.IntegerField(
        choices=((1, 1), (2, 2)),
        blank=True,
        null=True,
        verbose_name=_("Anzahl der Keimblätter"),
    )
    att_axis = models.CharField(
        max_length=3,
        choices=AXIS_CHOICES,
        blank=True,
        verbose_name=_("Anheftung an Sprossachse"),
    )
    sheath = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Blattscheide"),
        help_text='Gib "Nicht vorhanden" ein falls es wichtig ist, dass dieses Merkmal nicht ausgeprägt ist.',
    )
    pos_axis = models.CharField(
        max_length=3,
        choices=POS_CHOICES,
        blank=True,
        verbose_name=_("Stellung an Sprossachse"),
    )

    spr_whole = models.CharField(
        max_length=3,
        choices=SPR_WHOLE_CHOICES,
        blank=True,
        verbose_name=_("Blattspreite gesamt"),
    )
    dep_cuts = models.CharField(
        max_length=3,
        choices=CUT_CHOICES,
        blank=True,
        verbose_name=_("Tiefe von Einschnitten"),
    )
    arr_cuts = models.CharField(
        max_length=3,
        choices=ARR_CHOICES,
        blank=True,
        verbose_name=_("Anordnung von Einschnitten/Blättchen"),
    )
    arr_special = models.BooleanField(
        default=False, verbose_name=_("Anordnung ist buchtig.")
    )
    form = models.CharField(
        max_length=3,
        choices=FORM_CHOICES,
        blank=True,
        verbose_name=_("Gestalt des Blattes/der Blättchen"),
    )
    count = models.CharField(
        max_length=200, blank=True, verbose_name=_("Anzahl Blättchen")
    )
    leaflets = models.CharField(
        max_length=3,
        choices=LEAFLET_CHOICES,
        blank=True,
        verbose_name=_("Spreiten/Blättchen"),
    )
    texture = models.CharField(
        max_length=3,
        choices=TEXTURE_CHOICES,
        blank=True,
        verbose_name=_("Beschaffenheit"),
    )
    sur_texture = models.CharField(
        max_length=3,
        choices=SUR_TEXTURE_CHOICES,
        blank=True,
        verbose_name=_("Oberflächenbeschaffenheit"),
    )
    side_leaf = models.CharField(
        max_length=3, choices=SIDE_CHOICES, blank=True, verbose_name=_("Nebenblattrand")
    )
    diam = models.CharField(
        max_length=3, choices=DIAM_CHOICES, blank=True, verbose_name=_("Querschnitt")
    )
    sp_ground = models.CharField(
        max_length=3, choices=SP_CHOICES, blank=True, verbose_name=_("Spreitengrund")
    )
    sp_top = models.CharField(
        max_length=3,
        choices=SP_TOP_CHOICES,
        blank=True,
        verbose_name=_("Spreitengrund"),
    )
    specialty = models.CharField(
        max_length=200,
        blank=True,
        verbose_name=_("Besondere Merkmale"),
        help_text='Gib "Nicht vorhanden" ein falls es wichtig ist, dass dieses Merkmal nicht ausgeprägt ist.',
    )

    plant = models.OneToOneField(
        Plant, related_name="leaf", on_delete=models.CASCADE, verbose_name=_("Pflanze")
    )


class Sprout(models.Model):

    appear = models.CharField(
        max_length=1,
        choices=(("k", _("krautig")), ("h", _("holzig"))),
        blank=True,
        verbose_name=_("Erscheinung"),
    )
    pos = models.CharField(
        max_length=3, choices=POSITION_CHOICES, blank=True, verbose_name=_("Stellung")
    )
    thick_flesh = models.BooleanField(default=False, verbose_name=_("Dickfleischig"))
    milk = models.BooleanField(default=False, verbose_name=_("Milchsaft"))
    rose = models.BooleanField(default=False, verbose_name=_("Grundblattrose"))
    leafly = models.CharField(
        max_length=3,
        choices=(("nur", _("Nur am Grund")), ("auc", _("Auch über Grund"))),
        blank=True,
        verbose_name=_("Beblätterung"),
    )
    diam = models.CharField(
        max_length=3, choices=SP_DIAM_CHOICES, blank=True, verbose_name=_("Stellung")
    )
    sur_texture = models.CharField(
        max_length=3,
        choices=SUR_TEXTURE_CHOICES,
        blank=True,
        verbose_name=_("Oberflächenbeschaffenheit"),
    )

    blade = models.CharField(max_length=200, blank=True, verbose_name=_("Halm"))
    cluster = models.CharField(max_length=200, blank=True, verbose_name=_("Horst"))

    plant = models.OneToOneField(
        Plant,
        on_delete=models.CASCADE,
        related_name="sprout",
        verbose_name=_("Pflanze"),
    )


class Fruit(models.Model):

    spread = models.CharField(
        max_length=2,
        choices=SPREAD_CHOICES,
        blank=True,
        verbose_name=_("Ausbreitungsform"),
    )
    pos = models.CharField(
        max_length=2,
        choices=FRUIT_POS_CHOICES,
        blank=True,
        verbose_name=_("Lage der Samenanlage"),
    )
    type = models.CharField(
        max_length=3, choices=TYPE_CHOICES, blank=True, verbose_name=_("Fruchttyp")
    )

    cnt = models.CharField(max_length=200, blank=True, verbose_name=_("Samenzahl"))
    form = models.CharField(max_length=200, blank=True, verbose_name=_("Form"))
    wings = models.CharField(
        max_length=200,
        blank=True,
        verbose_name=_("Beflügelung"),
        help_text='Gib "Nicht vorhanden" ein falls es wichtig ist, dass dieses Merkmal nicht ausgeprägt ist.',
    )
    wings_spec = models.CharField(
        max_length=200, blank=True, verbose_name=_("Beflügelung Besonderheit")
    )

    plant = models.OneToOneField(
        Plant, on_delete=models.CASCADE, related_name="fruit", verbose_name=_("Pflanze")
    )


class Blossom(models.Model):

    type = models.CharField(
        max_length=3,
        choices=BL_TYPE_CHOICES,
        blank=True,
        verbose_name=_("Blütenstandtyp"),
    )
    bl_cnt = models.CharField(
        max_length=100, blank=True, verbose_name=_("Blüten pro Blütenstand")
    )
    sym = models.CharField(
        max_length=1, choices=SYM_CHOICES, blank=True, verbose_name=_("Symmetrie")
    )
    parting = models.CharField(
        max_length=3, choices=PART_CHOICES, blank=True, verbose_name=_("Blütenstandtyp")
    )
    cnt = models.IntegerField(
        choices=((3, 3), (4, 4), (5, 5)),
        blank=True,
        null=True,
        verbose_name=_("Zähligkeit"),
    )
    hull = models.CharField(
        max_length=3, choices=HULL_CHOICES, blank=True, verbose_name=_("Blütenstandtyp")
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

    crown_color = models.CharField(max_length=100, blank=True, verbose_name=_("Farbe"))
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
        verbose_name=_("Frucht Ständigkeit"),
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
    griffel_sub = models.BooleanField(
        default=False, verbose_name=_("Ständigkeit des Griffels ist sub-")
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
    blos = models.CharField(max_length=100, blank=True, verbose_name=_("Blütig"))
    straw_ground = models.CharField(
        max_length=2,
        choices=GROUND_CHOICES,
        blank=True,
        verbose_name=_("Ansatz an Halm"),
    )
    order = models.CharField(
        max_length=100, blank=True, verbose_name=_("Ähren pro Ährchen ")
    )
    aer_per_aer = models.CharField(
        max_length=100, blank=True, verbose_name=_("Anordnung ")
    )
    aer_per_ab = models.CharField(
        max_length=100, blank=True, verbose_name=_("Ährchen pro Absatz")
    )

    plant = models.OneToOneField(
        Plant,
        on_delete=models.CASCADE,
        related_name="blossom",
        verbose_name=_("Pflanze"),
    )


# Model for the tree representation of the profiles
class TreeNode(MPTTModel):
    node_name = models.CharField(
        max_length=200, verbose_name=_("node name"), unique=True
    )
    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="leaf_nodes",
    )

    info_text = models.TextField(max_length=500, blank=True)
    is_top_level = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Tree Node")
        verbose_name_plural = _("Tree Nodes")

    def __str__(self):
        return self.node_name
