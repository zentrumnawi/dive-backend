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


class Leaf(models.Model):

    NERV_CHOICES = (
        ("str", _("streifennervig")),
        ("net", _("netznervig")),
        ("fie", _("fiedernervig")),
        ("fin", _("fingernervig")),
        ("fus", _("fußnervig")),
        ("gab", _("gabelnervig"))
    )
    AXIS_CHOICES = (
        ("ges", _("gestielt")),
        ("sit", _("sitzend/ungestielt")),
        ("ste", _("stengelumfassend")),
        ("hal", _("halbstengelumfassend")),
        ("dur", _("durchwachsen")),
        ("ver", _("verwachsen")),
        ("sch", _("scheidig verwachsen")),
        ("her", _("herablaufend")),
        ("rei", _("reitend")),
        ("hin", _("hinfällig"))
    )
    POS_CHOICES = (
        ("gru", _("grundständig")),
        ("wec", _("wechselständig/spiralig")),
        ("zwe", _("zweizeilig/distich")),
        ("dre", _("dreizeilig/tristich")),
        ("geg", _("gegenständig")),
        ("kre", _("kreuzgegenständig/dekussiert")),
        ("gep", _("gepaart")),
        ("qui", _("quirlig/wirtelig")),
        ("sch", _("scheinquirlig")),
        ("dac", _("dachziegelig")),
        ("ein", _("einseitig")),
        ("ges", _("gescheitelt"))
    )
    SPR_WHOLE_CHOICES = (
        ("ein", _("einfach")),
        ("zus", _("zusammengesetzt"))
    )
    CUT_CHOICES = (
        ("gan", _("ganz/ungeteilt")),
        ("gel", _("gelappt")),
        ("gep", _("gespalten")),
        ("get", _("geteilt")),
        ("ges", _("geschnitten"))
    )
    ARR_CHOICES = (
        ("han", _("handförmig/fingerförmig")),
        ("hgl", _("handförmig gelappt")),
        ("hgt", _("handförmig geteilt")),
        ("hgs", _("handförmig geschnitten")),
        ("gef", _("gefingert")),
        ("fie", _("fiederförmig/fiederig")),
        ("fil", _("fiederlappig")),
        ("fip", _("fiederspaltig")),
        ("fit", _("fiederteilig")),
        ("fis", _("fiederschnittig")),
        ("paa", _("paarig gefiedert")),
        ("unp", _("unpaarig gefiedert")),
        ("unf", _("unterbrochen fiederschnittig")),
        ("ung", _("unterbrochen gefiedert")),
        ("dog", _("doppelt gefiedert")),
        ("meh", _("mehrfach gefiedert")),
        ("dre", _("dreizählig")),
        ("dod", _("doppelt dreizählig")),
        ("lei", _("leierförmig")),
        ("sch", _("schrotsägeförmig")),
        ("kam", _("kammförmig")),
        ("fug", _("fußförmig geschnitten")),
        ("fuz", _("fußförmig zusammengesetzt"))
    )
    FORM_CHOICES = (
        ("kre", _("kreisrund")),
        ("run", _("rundlich")),
        ("ell", _("elliptisch")),
        ("eif", _("eiförmig")),
        ("ver", _("verkehrteiförmig")),
        ("spa", _("spatelförmig/spatelig")),
        ("len", _("lanzettlich")),
        ("eil", _("eilanzettlich")),
        ("lae", _("länglich")),
        ("lin", _("linealisch/lineal")),
        ("nad", _("nadelförmig")),
        ("pfr", _("pfriemlich")),
        ("bor", _("borstenförmig/borstlich")),
        ("fad", _("fadenförmig/fädlich")),
        ("bin", _("binsenartig")),
        ("roe", _("röhrig")),
        ("ser", _("schwertförmig")),
        ("dre", _("dreieckig")),
        ("kei", _("keilförmig")),
        ("rau", _("rautenförmig/rhombisch")),
        ("her", _("herzförmig")),
        ("vhe", _("verkehrtherzförmig")),
        ("nie", _("nierenförmig")),
        ("pfe", _("pfeilförmig")),
        ("spi", _("spießförmig")),
        ("gei", _("geigenförmig")),
        ("sup", _("schuppenförmig")),
        ("sil", _("schildförmig"))
    )
    LEAFLET_CHOICES = (
        ("gan", _("ganzrandig")),
        ("ges", _("gesägt")),
        ("dop", _("doppelt gesägt")),
        ("rue", _("rückwärts gesägt")),
        ("gez", _("gezähnt")),
        ("gzt", _("gezähnelt")),
        ("gef", _("gefranst")),
        ("gek", _("gekerbt")),
        ("geb", _("gebuchtet")),
        ("ges", _("geschweift")),
        ("bew", _("bewimpert")),
        ("vor", _("vorwärts rauh")),
        ("rra", _("rückwärts rauh"))
    )
    TEXTURE_CHOICES = (
        ("kra", _("krautig")),
        ("fle", _("fleischig")),
        ("led", _("lederig")),
        ("hae", _("häutig/trockenhäutig")),
        ("imm", _("immergrün")),
        ("sta", _("starr/steif"))
    )
    SUR_TEXTURE_CHOICES = (
        ("gla", _("glatt")),
        ("run", _("runzelig")),
        ("rau", _("rauh")),
        ("vra", _("vorwärts rauh")),
        ("ber", _("bereift")),
        ("bes", _("bestäubt/bemehlt")),
        ("pap", _("papillös")),
        ("pun", _("punktiert")),
        ("swi", _("schwielig")),
        ("kah", _("kahl")),
        ("ver", _("verkahlend")),
        ("fla", _("flaumhaarig/weichhaarig")),
        ("sei", _("seidenhaarig")),
        ("spi", _("spinnwebig")),
        ("flo", _("flockig")),
        ("sam", _("samthaarig")),
        ("fil", _("filzig")),
        ("wol", _("wollig")),
        ("zot", _("zottig")),
        ("rah", _("rauhaarig")),
        ("ste", _("steifhaarig")),
        ("gew", _("gewimpert")),
        ("dru", _("drüsenhaarig")),
        ("ste", _("sternhaarig")),
        ("sdh", _("schildhaarig")),
        ("sup", _("schuppenhaarig/schuppig")),
        ("sue", _("schülferig")),
        ("bae", _("bärtig")),
        ("ach", _("achselbärtig")),
        ("nac", _("nackt"))
    )
    SIDE_CHOICES = (
        ("gan", _("ganzrandig")),
        ("ges", _("gesägt")),
        ("dop", _("doppelt gesägt")),
        ("rue", _("rückwärts gesägt")),
        ("gez", _("gezähnt")),
        ("gzt", _("gezähnelt")),
        ("gef", _("gefranst")),
        ("gek", _("gekerbt")),
        ("geb", _("gebuchtet")),
        ("gew", _("geschweift")),
        ("bew", _("bewimpert")),
        ("vor", _("vorwärts rauh")),
        ("rur", _("rückwärts rauh"))
    )
    DIAM_CHOICES = (
        ("zur", _("zurückgerollt/umgerollt")),
        ("ein", _("eingerollt")),
        ("zus", _("zusammengerollt")),
        ("gef", _("gefalzt/gefaltet")),
        ("rin", _("rinnig")),
        ("gek", _("gekielt")),
        ("dop", _("doppelrillig"))
    )
    SP_CHOICES = (
        ("kei", _("keilig/keilförmig")),
        ("ver", _("verschmälert")),
        ("abg", _("abgerundet")),
        ("ges", _("gestutzt")),
        ("her", _("herzförmig")),
        ("nie", _("nierenförmig")),
        ("pfe", _("pfeilförmig")),
        ("spi", _("spießförmig"))
    )
    SP_TOP_CHOICES = (
        ("abg", _("abgerundet")),
        ("ges", _("gestzutzt")),
        ("stu", _("stumpf")),
        ("spi", _("spitz")),
        ("zug", _("zugespitzt")),
        ("beg", _("begrannt")),
        ("sta", _("stachelspitze")),
        ("haa", _("haarspitzig")),
        ("bes", _("bespitzt")),
        ("aus", _("ausgerandet")),
    )
    nerves = models.CharField(max_length=3, choices=NERV_CHOICES, verbose_name=_("Blattnerven"))
    cnt_germ = models.IntegerField(choices=((1,1), (2,2)), verbose_name=_("Anzahl der Keimblätter"))
    att_axis = models.CharField(max_length=3, choices=AXIS_CHOICES, verbose_name=_("Anheftung an Sprossachse"))
    sheath = models.CharField(max_length=100, default="-", verbose_name=_("Blattscheide"))
    pos_axis = models.CharField(max_length=3, choices=POS_CHOICES, verbose_name=_("Stellung an Sprossachse"))

    spr_whole = models.CharField(max_length=3, choices=SPR_WHOLE_CHOICES, verbose_name=_("Blattspreite gesamt"))
    dep_cuts = models.CharField(max_length=3, choices=CUT_CHOICES, verbose_name=_("Tiefe von Einschnitten"))
    arr_cuts = models.CharField(max_length=3, choices=ARR_CHOICES, verbose_name=_("Anordnung von Einschnitten/Blättchen"))
    arr_special = models.BooleanField(default=False, verbose_name=_("Anordnung ist buchtig."))
    form = models.CharField(max_length=3, choices=FORM_CHOICES, verbose_name=_("Gestalt des Blattes/der Blättchen"))
    count = models.CharField(max_length=200, default="", verbose_name=_("Anzahl Blättchen"))
    leaflets = models.CharField(max_length=3, choices=LEAFLET_CHOICES, verbose_name=_("Spreiten/Blättchen"))
    texture = models.CharField(max_length=3, choices=TEXTURE_CHOICES, verbose_name=_("Beschaffenheit"))
    sur_texture = models.CharField(max_length=3, choices=SUR_TEXTURE_CHOICES, verbose_name=_("Oberflächenbeschaffenheit"))
    side_leaf = models.CharField(max_length=3, choices=SIDE_CHOICES, verbose_name=_("Nebenblattrand"))
    diam = models.CharField(max_length=3, choices=DIAM_CHOICES, verbose_name=_("Querschnitt"))
    sp_ground = models.CharField(max_length=3, choices=SP_CHOICES, verbose_name=_("Spreitengrund"))
    sp_top = models.CharField(max_length=3, choices=SP_TOP_CHOICES, verbose_name=_("Spreitengrund"))
    specialty = models.CharField(max_length=200, default="", verbose_name=_("Besondere Merkmale"))

    plant = models.OneToOneField(Plant, related_name="leaf", on_delete=models.CASCADE, verbose_name=_("Pflanze"))


class Sprout(models.Model):
    POSITION_CHOICES = (
        ("auf", _("aufrecht")),
        ("aua", _("aufrecht-abstehend")),
        ("abs", _("abstehend")),
        ("spa", _("sparrig")),
        ("zur", _("zurückgeschlagen")),
        ("lie", _("liegend")),
        ("kri", _("kriechend")),
        ("aus", _("aufsteigend/aufstrebend")),
        ("gek", _("gekniet")),
        ("ueb", _("übergebogen")),
        ("nic", _("nickend")),
        ("hae", _("hängend")),
        ("flu", _("flutend")),
        ("Ran", _("Rankenpflanze")),
        ("Win", _("Windepflanze")),
        ("Spr", _("Spreizklimmer")),
        ("Wur", _("Wurzelkletterer")),
        ("hor", _("horstig")),
        ("loc", _("lockerrasig"))
    )
    SP_DIAM_CHOICES = (
        ("sti", _("stielrund")),
        ("hal", _("halbstielrund")),
        ("zus", _("zusammengedrückt")),
        ("zwe", _("zweischneidig")),
        ("kan", _("kantig")),
        ("stu", _("stumpfkantig")),
        ("ger", _("gerieft /gerillt")),
        ("gef", _("gefurcht")),
        ("kan", _("kantig gefurcht /scharfkantig")),
        ("gri", _("gerippt")),
        ("gfl", _("geflügelt")),
        ("kno", _("knotig"))
    )
    SUR_TEXTURE_CHOICES = (
        ("gla", _("glatt")),
        ("run", _("runzelig")),
        ("rau", _("rauh")),
        ("vra", _("vorwärts rauh")),
        ("ber", _("bereift")),
        ("bes", _("bestäubt/bemehlt")),
        ("pap", _("papillös")),
        ("pun", _("punktiert")),
        ("swi", _("schwielig")),
        ("kah", _("kahl")),
        ("ver", _("verkahlend")),
        ("fla", _("flaumhaarig/weichhaarig")),
        ("sei", _("seidenhaarig")),
        ("spi", _("spinnwebig")),
        ("flo", _("flockig")),
        ("sam", _("samthaarig")),
        ("fil", _("filzig")),
        ("wol", _("wollig")),
        ("zot", _("zottig")),
        ("rah", _("rauhaarig")),
        ("ste", _("steifhaarig")),
        ("gew", _("gewimpert")),
        ("dru", _("drüsenhaarig")),
        ("ste", _("sternhaarig")),
        ("sdh", _("schildhaarig")),
        ("sup", _("schuppenhaarig/schuppig")),
        ("sue", _("schülferig")),
        ("bae", _("bärtig")),
        ("ach", _("achselbärtig")),
        ("nac", _("nackt"))
    )
    appear = models.CharField(max_length=1, choices=(("k", _("krautig")),("h", _("holzig"))), default="",verbose_name=_("Erscheinung"))
    pos = models.CharField(max_length=3, choices=POSITION_CHOICES, verbose_name=_("Stellung"))
    thick_flesh = models.BooleanField(default=False, verbose_name=_("Dickfleischig"))
    milk = models.BooleanField(default=False, verbose_name=_("Milchsaft"))
    rose = models.BooleanField(default=False, verbose_name=_("Grundblattrose"))
    leafly = models.CharField(max_length=3, choices=(("nur", _("Nur am Grund")),("auc", _("Auch über Grund"))), verbose_name=_("Beblätterung"))
    diam = models.CharField(max_length=3, choices=SP_DIAM_CHOICES, verbose_name=_("Stellung"))
    sur_texture = models.CharField(max_length=3, choices=SUR_TEXTURE_CHOICES, verbose_name=_("Oberflächenbeschaffenheit"))

    blade = models.CharField(max_length=200, default="", verbose_name=_("Halm"))
    cluster = models.CharField(max_length=200, default="", verbose_name=_("Horst"))

    plant = models.OneToOneField(Plant, on_delete=models.CASCADE, related_name="sprout", verbose_name=_("Pflanze"))

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
