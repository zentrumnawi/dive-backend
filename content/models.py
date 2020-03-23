from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import ugettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey

# Custom Models, representing the actual data of a profile, implement here.
# At least one model needs to have a ForeignKey field to the TreeNode model
# with related_name="profiles". If not, the profiles endpoint will throw an
# error.


class Plant(models.Model):

    HABITAT_CHOICES = (
        ("sch", _("Schlammfluren")),
        ("roe", _("Röhrichte")),
        ("sae", _("Säume")),
        ("sta", _("Stauden")),
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
        ("ufe", _("Ufer"))
    )
    STATUS_CHOICES = (
        ("e", _("einheimisch")),
        ("a", _("Archaeophyt")),
        ("n", _("Neophyt"))
    )
    INTERACTION_CHOICES = (
        ("par", _("parasitisch")),
        ("nip", _("nicht parasitisch")),
        ("obl", _("obligate Mykorrhiza")),
        ("fak", _("fakultative Mykorrhiza"))
    )
    GROUND_CHOICES = (
        ("rei", _("nährstoffreich")),
        ("arm", _("nährstoffarm")),
        ("leh", _("lehmig")),
        ("tor", _("torfig")),
        ("san", _("sandig")),
        ("ste", _("steinig/felsig"))
    )
    ROOT_CHOICES = (
        ("erh", _("erhalten")),
        ("ers", _("ersetzt durch sprossbürtige Wurzeln"))
    )

    name = models.CharField(max_length=100, verbose_name=_("Art"))
    trivial_name = models.CharField(max_length=100, verbose_name=_("Trivialname"))
    habitat = ArrayField(base_field=models.CharField(max_length=3, choices=HABITAT_CHOICES), blank=True, verbose_name=_("Lebensraum"))
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name=_("Status"))
    interaction = models.CharField(max_length=3, choices=INTERACTION_CHOICES, verbose_name=_("Interaktionen"))
    ground = ArrayField(base_field=models.CharField(max_length=3, choices=GROUND_CHOICES), blank=True, verbose_name=_("Untergrund"))
    bloom = models.CharField(max_length=200, verbose_name=_("Blütezeit"))

    prime_root = models.CharField(max_length=3, choices=ROOT_CHOICES, verbose_name=_("Primärwurzel"))
    nodule = models.BooleanField(verbose_name=_("Wurzelknollen"))

    systematics = models.ForeignKey("TreeNode", related_name="profiles", on_delete=models.DO_NOTHING, null=True, verbose_name=_("Steckbrief-Ebene"))


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
