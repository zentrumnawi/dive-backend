from django.utils.translation import ugettext_lazy as _


def normalize_choices_term(item):
    # Normalize term to support sortring according to DIN 5007-1
    term = f"{item[1]}"
    term = term.lower()
    for char, replacement_char in (
        ("ä", "a"),
        ("ö", "o"),
        ("ü", "u"),
        ("ß", "ss"),
        (" ", ""),
        ("-", ""),
        ("/", ""),
    ):
        term = term.replace(char, replacement_char)

    return term


# Plant choices ------------------------------------------------------------------------
# general (sentence 1) -----------------------------------------------------------------
ARTICLE_CHOICES = (("", "-"), ("der", _("der")), ("die", _("die")), ("das", _("das")))
GROWTH_FORM_SUBCHOICES = [()] * 2
GROWTH_FORM_SUBCHOICES[0] = (  # ein
    ("bau", _("Baum")),
    ("hal", _("Halbstrauch")),
    ("kra", _("Kraut")),
    ("krc", _("krautiger Chemaephyt")),
    ("scs", _("Scheinstrauch")),
    ("spa", _("Spalierstrauch")),
    ("spr", _("Spreizklimmer")),
    ("sta", _("Staudenstrauch")),
    ("str", _("Strauch")),
    ("stb", _("Strauchbaum")),
    ("zwe", _("Zwergstrauch")),
)
GROWTH_FORM_SUBCHOICES[1] = (  # eine
    ("kle", _("Kletterpflanze")),
    ("lia", _("Liane")),
    ("sch", _("Schwimmpflanze")),
    ("tau", _("Tauchpflanze")),
)
GROWTH_FORM_CHOICES = [
    *GROWTH_FORM_SUBCHOICES[0],
    *GROWTH_FORM_SUBCHOICES[1],
]
GROWTH_FORM_CHOICES.sort(key=normalize_choices_term)
GROWTH_HEIGHT_UNITS = (("m", "m"), ("cm", "cm"))
# general (sentence 2) -----------------------------------------------------------------
INTERACTION_CHOICES = (
    ("par", _("parasitisch")),
    ("nip", _("nicht parasitisch")),
    ("obl", _("obligat Mykorrhiza-bildend")),
    ("fak", _("fakultativ Mykorrhiza-bildend")),
)
DISPERSAL_FORM_CHOICES = (
    ("na", _("Nacktsamer")),
    ("be", _("Bedecktsamer")),
    ("sp", _("Sporenpflanze")),
)
GROUND_CHOICES = (
    (1, _("kalkfrei, basisch")),
    (2, _("kalkarm")),
    (3, _("feucht, zum Teil periodisch überschwemmt")),
    (4, _("frisch bis feucht, meist nährstoffreich")),
    (5, _("frisch und nährstoffreich")),
    (6, _("lehmig bis tonig")),
    (7, _("mäßig nährstoffreich")),
    (8, _("nährstoff(stickstoff)reich")),
    (9, _("nährstoffreich")),
)
HABITATS_SUBCHOICES = [()] * 3
HABITATS_SUBCHOICES[0] = (  # an
    _("Auengebüschsäume"),
    _("Auenwaldsäume"),
    _("Bäche"),
    _("Bachränder"),
    _("Felsen"),
    _("Grabenränder"),
    _("Hänge"),
    _("Heckenränder"),
    _("Laubmischwaldsäume"),
    _("Mauern"),
    _("Quellen"),
    _("Säume"),
    _("Talhänge"),
    _("Trockengebüschsäume"),
    _("Trockenwaldsäume"),
    _("Ufer"),
    _("Waldquellen"),
    _("Waldränder"),
    _("Waldsäume"),
    _("Waldwegränder"),
    _("Wegränder"),
)
HABITATS_SUBCHOICES[1] = (  # in
    _("Ansaaten"),
    _("Auengebüsche"),
    _("Auenwälder"),
    _("Bruchwälder"),
    _("Buchenwälder"),
    _("Eichen-Hainbuchen-Wälder"),
    _("Ephemerenfluren"),
    _("Erlenwälder"),
    _("Flussuferstaudenfluren"),
    _("Forste"),
    _("Gärten"),
    _("Gebüsche"),
    _("Gebüschsäume"),
    _("Gräben"),
    _("Hackkulturen"),
    _("Hangwälder"),
    _("Hecken"),
    _("Heiden"),
    _("Hochgrasfluren"),
    _("Hochstaudenfluren"),
    _("Kalkfelsenfluren"),
    _("Kiesgruben"),
    _("Laubmischwälder"),
    _("Laubwälder"),
    _("Mischwälder"),
    _("Moorwälder"),
    _("Nadelholzforste"),
    _("Nadelwälder"),
    _("Parkanlagen"),
    _("Parks"),
    _("Pioniergehölze"),
    _("Quellmoore"),
    _("Rasenansaaten"),
    _("Robinienforste"),
    _("Röhrichte"),
    _("Schläge"),
    _("Schlaggehölze"),
    _("Schlammfluren"),
    _("Schluchtwälder"),
    _("Staudenfluren"),
    _("Steinbrüche"),
    _("Steinschuttfluren"),
    _("Uferstaudenfluren"),
    _("Vorwälder"),
    _("Vorwaldgehölze"),
    _("Wälder"),
    _("Waldschläge"),
    _("Waldverlichtungen"),
    _("Weinberge"),
)
HABITATS_SUBCHOICES[2] = (  # auf
    _("Äcker"),
    _("Bahnanlagen"),
    _("Brachen"),
    _("Dämme"),
    _("Fettwiesen"),
    _("Friedhöfe"),
    _("Frischwiesen"),
    _("Grünlandbrachen"),
    _("Halbtrockenrasen"),
    _("Intensivgrünländer"),
    _("Kalktrockenrasen"),
    _("Kleeäcker"),
    _("Magerrasen"),
    _("Magerweiden"),
    _("Obstwiesen"),
    _("Parkrasen"),
    _("Rasen"),
    _("Ruderalflächen"),
    _("Sandtrockenrasen (Küstendünen)"),
    _("Schutt"),
    _("Schutthalden"),
    _("Silikatmagerrasen"),
    _("Steinriegel"),
    _("Sumpfwiesen"),
    _("Trittrasen"),
    _("Trittstellen"),
    _("Trockenrasen"),
    _("Verlichtungen"),
    _("Viehläger"),
    _("Waldlichtungen"),
    _("Waldwege"),
    _("Weiden"),
    _("Wiesen"),
    _("Xerothermrasen"),
)
HABITATS_SUBCHOICES[0] = tuple(zip(range(100, 199), HABITATS_SUBCHOICES[0]))
HABITATS_SUBCHOICES[1] = tuple(zip(range(200, 299), HABITATS_SUBCHOICES[1]))
HABITATS_SUBCHOICES[2] = tuple(zip(range(300, 399), HABITATS_SUBCHOICES[2]))
HABITATS_CHOICES = [
    *HABITATS_SUBCHOICES[0],
    *HABITATS_SUBCHOICES[1],
    *HABITATS_SUBCHOICES[2],
]
HABITATS_CHOICES.sort(key=normalize_choices_term)
RUDERAL_SITES_CHOICES = (
    _("Bahnanlagen"),
    _("Bahndämme"),
    _("Böschungen"),
    _("Bruchwälder"),
    _("Dämme"),
    _("Geröllstände"),
    _("Gleitschotter"),
    _("Gräben"),
    _("Kiesgruben"),
    _("an Mauern"),
    _("Pflasterfugen"),
    _("Schutt"),
    _("Steinbrüche"),
    _("Straßenböschungen"),
    _("Tagebaue"),
    _("Trittstellen"),
    _("Waldränder"),
    _("Waldschläge"),
    _("Wegränder"),
    _("Xerothermrasen"),
    _("an Zäunen"),
)
RUDERAL_SITES_CHOICES = tuple(zip(range(1, 99), RUDERAL_SITES_CHOICES))
# general (sentence 3) -----------------------------------------------------------------
LIFE_FORM_CHOICES = (
    ("pha", _("Phanerophyt")),
    ("cha", _("Chamaephyt")),
    ("hem", _("Hemikryptophyt")),
    ("kry", _("Kryptophyt")),
    ("the", _("Therophyt")),
    ("geo", _("Geophyt")),
    ("hel", _("Helophyt (Sumpfpflanze)")),
    ("hyd", _("Hydrophyt (Wasserpflanze)")),
)
STATUS_CHOICES = (
    ("e", _("einheimisch")),
    ("a", _("Archaeophyt")),
    ("n", _("Neophyt")),
)
# --------------------------------------------------------------------------------------


# Leaf choices -------------------------------------------------------------------------
# general ------------------------------------------------------------------------------
VENATION_CHOICES = (
    ("fie", _("fiedernervig")),
    ("fin", _("fingernervig")),
    ("fus", _("fußnervig")),
    ("gab", _("gabelnervig")),
    ("net", _("netznervig")),
    ("str", _("streifennervig")),
)
DIVISION_CHOICES = (("ein", _("einfach")), ("zus", _("zusammengesetzt")))
SUCCULENCE_CHOICES = (("dic", _("dickfleischig")), (("ndi"), _("nicht dickfleischig")))
TEXTURE_CHOICES = (
    ("fle", _("fleischig")),
    ("hae", _("häutig/trockenhäutig")),
    ("imm", _("immergrün")),
    ("kra", _("krautig")),
    ("led", _("lederig")),
    ("sta", _("starr/steif")),
)
CROSS_SECTION_CHOICES = (
    ("dop", _("doppelrillig")),
    ("ein", _("eingerollt")),
    ("gef", _("gefalzt/gefaltet")),
    ("gek", _("gekielt")),
    ("rin", _("rinnig")),
    ("zur", _("zurückgerollt/umgerollt")),
    ("zus", _("zusammengerollt")),
)
BASAL_LEAF_ROSETTE_CHOICES = (
    ("E", _("Erosulat")),
    ("H", _("Halbrosettenpflanze")),
    ("R", _("Rosettenpflanze")),
)
# attachment ---------------------------------------------------------------------------
ATTACHMENT_CHOICES = (
    ("dur", _("durchwachsen")),
    ("ges", _("gestielt")),
    ("hal", _("halbstengelumfassend")),
    ("her", _("herablaufend")),
    ("hin", _("hinfällig")),
    ("rei", _("reitend")),
    ("sch", _("scheidig verwachsen")),
    ("sit", _("sitzend/ungestielt")),
    ("ste", _("stengelumfassend")),
    ("ver", _("verwachsen")),
)
ARRANGMENT_CHOICES = (
    ("dac", _("dachziegelig")),
    ("dre", _("dreizeilig/tristich")),
    ("ein", _("einseitig")),
    ("geg", _("gegenständig")),
    ("gep", _("gepaart")),
    ("ges", _("gescheitelt")),
    ("gru", _("grundständig")),
    ("kre", _("kreuzgegenständig/dekussiert")),
    ("qui", _("quirlig/wirtelig")),
    ("sch", _("scheinquirlig")),
    ("wec", _("wechselständig/spiralig")),
    ("zwe", _("zweizeilig/distich")),
)
# lamina_compound_leaf -----------------------------------------------------------------
COMPOUND_LEAF_SHAPE_CHOICES = (
    ("dop", _("doppelt")),
    ("dod", _("doppelt dreizählig")),
    ("drz", _("dreizählig")),
    ("fif", _("fiederförmig")),
    ("fil", _("fiederlappig")),
    ("fis", _("fiederschnittig")),
    ("fip", _("fiederspaltig")),
    ("fit", _("fiederteilig")),
    ("fus", _("fußförmig")),
    ("gef", _("gefingert")),
    ("han", _("handförmig")),
    ("kam", _("kammförmig")),
    ("lei", _("leierförmig")),
    ("meh", _("mehrfach")),
    ("paa", _("paarig")),
    ("sch", _("schrotsägeförmig")),
    ("unp", _("unpaarig")),
    ("unt", _("unterbrochen")),
)
COMPOUND_LEAF_INCISION_DEPTH_CHOICES = (
    ("fis", _("fiederschnittig")),
    ("gan", _("ganz/ungeteilt")),
    ("fie", _("gefiedert")),
    ("gef", _("gefingert")),
    ("gel", _("gelappt")),
    ("ges", _("geschnitten")),
    ("gep", _("gespalten")),
    ("get", _("geteilt")),
    ("zus", _("zusammengesetzt")),
)
LEAFLET_INCISION_DEPTH_CHOICES = COMPOUND_LEAF_INCISION_DEPTH_CHOICES
# lamina_simple_leaf -------------------------------------------------------------------
SIMPLE_LEAF_SHAPE_CHOICES = (
    ("bin", _("binsenartig")),
    ("bor", _("borstenförmig/borstlich")),
    ("dre", _("dreieckig")),
    ("eif", _("eiförmig")),
    ("eil", _("eilanzettlich")),
    ("ell", _("elliptisch")),
    ("fad", _("fadenförmig/fädlich")),
    ("gei", _("geigenförmig")),
    ("her", _("herzförmig")),
    ("kei", _("keilförmig")),
    ("kre", _("kreisrund")),
    ("lae", _("länglich")),
    ("len", _("lanzettlich")),
    ("lin", _("linealisch/lineal")),
    ("nad", _("nadelförmig")),
    ("nie", _("nierenförmig")),
    ("pfe", _("pfeilförmig")),
    ("pfr", _("pfriemlich")),
    ("rau", _("rautenförmig/rhombisch")),
    ("roe", _("röhrig")),
    ("run", _("rundlich")),
    ("sil", _("schildförmig")),
    ("sup", _("schuppenförmig")),
    ("ser", _("schwertförmig")),
    ("spa", _("spatelförmig/spatelig")),
    ("spi", _("spießförmig")),
    ("ver", _("verkehrteiförmig")),
    ("vhe", _("verkehrtherzförmig")),
)
SIMPLE_LEAF_INCISION_DEPTH_CHOICES = (
    ("gan", _("ganz/ungeteilt")),
    ("gel", _("gelappt")),
    ("ges", _("geschnitten")),
    ("gep", _("gespalten")),
)
# lamina_general -----------------------------------------------------------------------
EDGE_CHOICES = (
    ("dor", _("dornig")),
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
    ("vor", _("vorwärts rau")),
    ("rur", _("rückwärts rau")),
)
SURFACE_CHOICES = (
    ("ach", _("achselbärtig")),
    ("bae", _("bärtig")),
    ("ber", _("bereift")),
    ("bes", _("bestäubt/bemehlt")),
    ("dru", _("drüsenhaarig")),
    ("fil", _("filzig")),
    ("fla", _("flaumhaarig/weichhaarig")),
    ("flo", _("flockig")),
    ("gew", _("gewimpert")),
    ("glz", _("glänzend")),
    ("gla", _("glatt")),
    ("kah", _("kahl")),
    ("nac", _("nackt")),
    ("pap", _("papillös")),
    ("pun", _("punktiert")),
    ("rau", _("rau")),
    ("rah", _("rauhaarig")),
    ("run", _("runzelig")),
    ("sam", _("samthaarig")),
    ("sdh", _("schildhaarig")),
    ("sue", _("schülferig")),
    ("sup", _("schuppenhaarig/schuppig")),
    ("swi", _("schwielig")),
    ("sei", _("seidenhaarig")),
    ("spi", _("spinnwebig")),
    ("ste", _("steifhaarig")),
    ("stn", _("sternhaarig")),
    ("ver", _("verkahlend")),
    ("vra", _("vorwärts rau")),
    ("wol", _("wollig")),
    ("zot", _("zottig")),
)
STIPULE_EDGE_CHOICES = EDGE_CHOICES
BASE_CHOICES = (
    ("kei", _("keilig/keilförmig")),
    ("ver", _("verschmälert")),
    ("abg", _("abgerundet")),
    ("ges", _("gestutzt")),
    ("her", _("herzförmig")),
    ("nie", _("nierenförmig")),
    ("pfe", _("pfeilförmig")),
    ("spi", _("spießförmig")),
)
APEX_CHOICES = (
    ("abg", _("abgerundet")),
    ("ges", _("gestutzt")),
    ("stu", _("stumpf")),
    ("spi", _("spitz")),
    ("zug", _("zugespitzt")),
    ("beg", _("begrannt")),
    ("sta", _("stachelspitz")),
    ("haa", _("haarspitzig")),
    ("bes", _("bespitzt")),
    ("aus", _("ausgerandet")),
)
# miscellaneous ------------------------------------------------------------------------
SEED_LEAF_NUMBER_CHOICES = ((1, 1), (2, 2))
# --------------------------------------------------------------------------------------


# LeafPoales choices -------------------------------------------------------------------
# overview -----------------------------------------------------------------------------
LEAFPOALES_SHAPE_CHOICES = (("f", _("flach")), ("r", _("röhrig")))
HAIRINESS_CHOICES = (
    ("kah", _("kahl")),
    ("sam", _("samtig")),
    ("lob", _("locker behaart")),
    ("beh", _("behaart")),
    ("dib", _("dicht behaart")),
    ("wol", _("wollig")),
)
LEAFPOALES_CROSS_SECTION_CHOICES = (
    ("Voa", _("Vogelflug-artig")),
    ("VPa", _("V-Profil-artig")),
    ("UPa", _("U-Profil-artig")),
    ("roe", _("röhrig")),
    ("run", _("rund")),
    ("abg", _("abgeflacht")),
    ("fla", _("flach")),
    ("bor", _("borstig")),
)
ALIGNMENT_NUM_CHOICES = (("", "-"), ("2", "2"), ("3", "3"), ("4", "4"))
ALIGNMENT_CHOICES = (
    ("", "---------"),
    ("-w", _("-wirtelig")),
    ("-z", _("-zeilig")),
)
ATTACHMENT_POINT_CHOICES = (("K", _("Knoten")), ("T", _("Triebgrund")))
# leaf_blade ---------------------------------------------------------------------------
BLADE_SHAPE_CHOICES = (
    ("bor", _("borstenförmig")),
    ("lan", _("lanzettlich")),
    ("lin", _("linealisch")),
    ("par", _("parallelrandig")),
    ("pfr", _("pfriemlich")),
)
BLADE_CORRUGATION_CHOICES = (
    ("gla", _("glatt")),
    ("gmS", _("glatt mit Skispur")),
    ("ung", _("undeutlich gerieft")),
    ("deg", _("deutlich gerieft")),
    ("ssg", _("sehr stark gerieft")),
)
BLADE_DOUBLE_GROOVE = (("m", _("mit Doppelrille")), ("o", _("ohne Doppelrille")))
BLADE_SHINE_CHOICES = (
    ("gla", _("glanzlos")),
    ("mag", _("matt glänzend")),
    ("seg", _("seidig glänzend")),
    ("stg", _("stark glänzend")),
)
BLADE_KEEL_CHOICES = (("m", _("mit auffälligem Kiel")), ("o", _("ohne Kiel")))
BLADE_EDGE_CHOICES = (
    ("gla", _("glatt")),
    ("vor", _("vorwärts rau")),
    ("rur", _("rückwärts rau")),
    ("bew", _("bewimpert")),
    ("bor", _("borstig")),
    ("gez", _("gezähnt")),
)
BLADE_BUD_SYSTEM_CHOICES = (("f", _("gefaltet")), ("r", _("gerollt")))
# leaf_base ----------------------------------------------------------------------------
BASE_EDGE_CHOICES = (("k", _("kahl")), ("b", _("behaart (< 3 mm)")))
BASE_AURICLE_CHOICES = (("m", _("mit Öhrchen")), ("o", _("ohne Öhrchen")))
# ligule -------------------------------------------------------------------------------
LIGULE_LENGTH_CHOICES = (
    ("kur", _("kurz")),
    ("mit", _("mittellang")),
    ("lan", _("lang")),
    ("sel", _("sehr lang")),
)
LIGULE_SHAPE_CHOICES = (
    ("abg", _("abgerundet")),
    ("aHa", _("als Haarkranz ausgebildet")),
    ("bew", _("bewimpert")),
    ("feh", _("fehlend")),
    ("ges", _("geschlitzt")),
    ("man", _("manschettenförmig")),
    ("roe", _("röhrenförmig")),
    ("sau", _("saumartig")),
    ("spi", _("spitz")),
    ("stu", _("stumpf")),
    ("zer", _("zerschlitzt")),
)
LIGULE_CONSISTENCY_CHOICES = (
    ("der", _("derb")),
    ("hae", _("häutig")),
    ("zar", _("zart")),
)
# leaf_sheath --------------------------------------------------------------------------
SHEATH_CONNATION_CHOICES = (
    ("off", _("offen")),
    ("iTv", _("in Teilen verwachsen")),
    ("fbo", _("fast bis oben geschlossen")),
    ("ges", _("geschlossen")),
)
# --------------------------------------------------------------------------------------


# Blossom choices ----------------------------------------------------------------------
# season -------------------------------------------------------------------------------
SEASON_CHOICES = ((None, "-"),) + tuple((x, x) for x in range(1, 13))
SEASON_DICT = {
    None: "",
    1: _("Januar"),
    2: _("Februar"),
    3: _("März"),
    4: _("April"),
    5: _("Mai"),
    6: _("Juni"),
    7: _("Juli"),
    8: _("August"),
    9: _("September"),
    10: _("Oktober"),
    11: _("November"),
    12: _("Dezember"),
}
# inflorescence ------------------------------------------------------------------------
INFLORESCENCE_TYPE_SUBCHOICES = [()] * 3
INFLORESCENCE_TYPE_SUBCHOICES[0] = (  # plural = singular
    ("bue", _("Büschel")),
    ("kae", _("Kätzchen")),
    ("kna", _("Knäuel")),
    ("kol", _("Kolben")),
    ("koc", _("Köpfchen")),
    ("krc", _("Körbchen")),
    ("zap", _("Zapfen")),
)
INFLORESCENCE_TYPE_SUBCHOICES[1] = (  # plural = singular + "n"
    ("aer", _("Ähre")),
    ("dol", _("Dolde")),
    ("dod", _("Doppeldolde")),
    ("dow", _("Doppelwickel")),
    ("ein", _("Einzelblüte")),
    ("ris", _("Rispe")),
    ("sca", _("Scheinähre")),
    ("scd", _("Scheindolde/Trugdolde")),
    ("scr", _("Schirmrispe")),
    ("sct", _("Schirmtraube")),
    ("spi", _("Spirre/Trichterrispe")),
    ("thy", _("Thyrse")),
    ("tra", _("Traube")),
    ("wic", _("Wickel")),
    ("zym", _("Zyme")),
)
INFLORESCENCE_TYPE_SUBCHOICES[2] = (  # pluaral -> PLURAL_DICT
    ("ebe", _("Ebenstrauß/Corymbus")),
    ("dic", _("Dichasium")),
    ("kop", _("Kopf")),
    ("kor", _("Korb")),
    ("mon", _("Monochasium")),
    ("ple", _("Pleiochasium")),
    ("scb", _("Scheinblüte/Pseudanthium")),
    ("scq", _("Scheinquirl")),
)
INFLORESCENCE_TYPE_PLURAL_DICT = {
    "ebe": _("Ebensträuße/Corymbusse"),
    "dic": _("Dichasien"),
    "kop": _("Köpfe"),
    "kor": _("Körbe"),
    "mon": _("Monochasien"),
    "ple": _("Pleiochasien"),
    "scb": _("Scheinblüten/Pseudanthien"),
    "scq": _("Scheinquirle"),
}
INFLORESCENCE_TYPE_CHOICES = [
    *INFLORESCENCE_TYPE_SUBCHOICES[0],
    *INFLORESCENCE_TYPE_SUBCHOICES[1],
    *INFLORESCENCE_TYPE_SUBCHOICES[2],
]
INFLORESCENCE_TYPE_CHOICES.sort(key=normalize_choices_term)
# general -----------------------------------------------------------------------------
MEROSITY_CHOICES = (
    ((None, "-"),) + tuple((x, x) for x in range(1, 9)) + ((9, _("viel")),)
)
MEROSITY_CHOICES_DICT = {**dict({None: ""}), **dict(MEROSITY_CHOICES[1:])}
SYMMETRY_CHOICES = (
    ("a", _("asymmetrisch")),
    ("d", _("disymmetrisch")),
    ("r", _("radiärsymmetrisch")),
    ("z", _("zygomorph")),
)
PERIANTH_CHOICES = (
    ("dop", _("doppelte Blütenhülle (Kalyx + Corolla)")),
    ("ein", _("einfache Blütenhülle (Perigon)")),
    ("feh", _("fehlende Blütenhülle")),
    ("lip", _("Lippenblüte")),
    ("roe", _("Röhrenblüte")),
    ("sch", _("Schmetterlingsblüte")),
    ("str", _("strahlende Randblüten")),
    ("zun", _("Zungenblüte")),
)
PERIANTH_SHAPE_CHOICES = (
    ("au", _("aufgeblasen")),
    ("as", _("ausgesackt")),
    ("ba", _("bauchig")),
    ("be", _("becherförmig")),
    ("gr", _("gespornt")),
    ("gl", _("glockig")),
    ("ke", _("keulig")),
    ("kr", _("krugförmig")),
    ("ku", _("kugelig")),
    ("na", _("napfförmig")),
    ("ra", _("radförmig")),
    ("ro", _("röhrig")),
    ("st", _("stielförmig")),
    ("tr", _("trichterförmig")),
    ("zu", _("zungenförmig")),
)
BRACT_SHAPE_SUBCHOICES = [()] * 3
BRACT_SHAPE_SUBCHOICES[0] = COMPOUND_LEAF_SHAPE_CHOICES
BRACT_SHAPE_SUBCHOICES[1] = SIMPLE_LEAF_SHAPE_CHOICES
BRACT_SHAPE_SUBCHOICES[2] = (("nvo", _("nicht vorhanden")),)
BRACT_SHAPE_CHOICES = [
    *BRACT_SHAPE_SUBCHOICES[0],
    *BRACT_SHAPE_SUBCHOICES[1],
    *BRACT_SHAPE_SUBCHOICES[2],
]
BRACT_SHAPE_CHOICES.sort(key=normalize_choices_term)
BLOSSOM_SEX_DISTRIBUTION_CHOICES = (
    ("e", _("eingeschlechtig")),
    ("s", _("steril")),
    ("z", _("zwittrig")),
)
PLANT_SEX_DISTRIBUTION_CHOICES = (
    ("e", _("einhäusig")),
    ("u", _("unvollständig zweihäusig")),
    ("z", _("zweihäusig")),
)
# sepal/petal --------------------------------------------------------------------------
CONNATION_NUMBER_CHOICES = (("", "-"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"))
CONNATION_TYPE_CHOICES = (
    ("", "---------"),
    ("-l", _("-lappig")),
    ("-s", _("-spaltig")),
    ("-t", _("-teilig")),
    ("-z", _("-zähnig")),
    ("fre", _("freiblättrig")),
    ("ver", _("verwachsenblättrig")),
    ("zwe", _("zweilippig")),
)
# sepal --------------------------------------------------------------------------------
SEPAL_CONNATION_CHOICES = (
    ("a", _("am Grund verwachsen")),
    ("u", _("unverwachsen")),
    ("v", _("verwachsen")),
)
# petal --------------------------------------------------------------------------------
PETAL_CONNATION_CHOICES = SEPAL_CONNATION_CHOICES
# tepal --------------------------------------------------------------------------------
TEPAL_CONNATION_CHOICES = SEPAL_CONNATION_CHOICES
# stamen -------------------------------------------------------------------------------
STAMEN_CONNATION_TYPE_CHOICES = (
    ("s", _("Staubfadenröhre")),
    ("v", _("verwachsen mit Kronblättern")),
)
# carpel -------------------------------------------------------------------------------
CARPEL_CONNATION_TYPE_CHOICES = (
    ("ap", _("apokarp")),
    ("co", _("coenokarp")),
    ("cp", _("coeno-parakarp")),
    ("cs", _("coeno-synkarp")),
    ("mo", _("monokarp")),
)
OVARY_POSITION_CHOICES = (
    ("ob", _("oberständig")),
    ("ho", _("halboberständig")),
    ("mi", _("mittelständig")),
    ("hu", _("halbunterständig")),
    ("un", _("unterständig")),
)
PISTIL_POSITION_CHOICES = (
    ("end", _("endständig")),
    ("gru", _("grundständig")),
    ("gyn", _("gynobasisch")),
    ("sei", _("seitenständig")),
    ("sen", _("subendständig")),
    ("sgr", _("subgrundständig")),
    ("sgy", _("subgynobasisch")),
    ("sse", _("subseitenständig")),
)
# --------------------------------------------------------------------------------------


# BlossomPoales choices ----------------------------------------------------------------
# inflorescence ------------------------------------------------------------------------
INFLORESCENCE_DENSITY_CHOICES = (
    ("l", _("locker")),
    ("d", _("in dichten Kopf zusammengezogen")),
)
INFLORESCENCE_POSITION_CHOICES = (
    ("a", _("aufrecht")),
    ("s", _("scheinbar seitenständig")),
)
BP_INFLORESCENCE_TYPE_CHOICES = (
    ("A", _("Ähre")),
    ("R", _("Rispe")),
    ("S", _("Spirre")),
)
# blossom_perianth ---------------------------------------------------------------------
BLOSSOM_SEX_CHOICES = (
    ("z", _("zwittrig")),
    ("s", _("zwittrig, selten einige weiblich")),
    ("e", _("eingeschlechtig")),
)
BP_PERIANTH_CHOICES = (
    ("m", _("mit Blütenhülle")),
    ("S", _("Blüte von Spelzen umgeben")),
)
# spikelet -----------------------------------------------------------------------------
SPIKELET_SHAPE_CHOICES = (
    ("zSv", _("zur Spitze hin verbreitert")),
    ("zus", _("zusammengedrückt")),
    ("sez", _("seitlich zusammengedrückt")),
    ("niz", _("nicht zusammengedrückt")),
)
SPIKELET_ATTACHMENT_CHOICES = (
    ("ges", _("gestielt")),
    ("bog", _("borstenlos gestielt")),
    ("vou", _("völlig ungestielt")),
    ("sit", _("sitzend")),
)
SPIKELET_SEX_CHOICES = (("z", _("zwittrig")), ("e", _("eingeschlechtig")))
SPIKELET_MAX_WIDTH_CHOICES = (
    ("un", _("unter der Mitte")),
    ("in", _("in der Mitte")),
    ("ue", _("über der Mitte")),
)
SPIKELET_RACHILLA_CHOICES = (
    ("gBa", _("glatt, zur Blütezeit abstehend")),
    ("sic", _("sichtbar")),
    ("zRs", _("zur Reife sichtbar")),
    ("nis", _("nicht sichtbar")),
)
SPIKELET_STALK_CHOICES = (
    ("lau", _("lang, unverzweigt")),
    ("lav", _("lang, verzweigt")),
    ("kur", _("kurz")),
    ("skv", _("sehr kurz, verzweigt")),
    ("vkA", _("viel kürzer als Ährchen")),
)
SPIKELET_SPINDLE_CHOICES = (
    ("z", _("zerbrechlich")),
    ("B", _("nach der Blütezeit zerbrechlich")),
    ("n", _("nicht zerbrechlich")),
)
# husks --------------------------------------------------------------------------------
HUSKS_FORM_CHOICES = (
    ("a", _("abgerundet")),
    ("R", _("auf dem Rücken abgerundet")),
    ("n", _("nicht abgerundet")),
)
HUSKS_KEEL_CHOICES = (("g", _("gekielt")), ("n", _("nicht gekielt")))
HUSKS_CROSS_SECTION_CHOICES = (
    ("o", _("oval")),
    ("r", _("rundlich")),
    ("s", _("2-schneidig")),
)
# --------------------------------------------------------------------------------------


# Fruit choices ------------------------------------------------------------------------
# fruit --------------------------------------------------------------------------------
FRUIT_TYPE_CHOICES = (
    ("ach", _("Achäne")),
    ("apf", _("Apfelfrucht")),
    ("bal", _("Balgfrucht")),
    ("bac", _("Balgfrüchtchen")),
    ("bee", _("Beere")),
    ("bru", _("Bruchfrucht")),
    ("dop", _("Doppelachäne")),
    ("glh", _("Gliederhülse")),
    ("gls", _("Gliederschote")),
    ("hue", _("Hülse")),
    ("kap", _("Kapsel")),
    ("kar", _("Karyopse")),
    ("kla", _("Klausenfrucht")),
    ("kok", _("Kokke")),
    ("nus", _("Nuss")),
    ("nue", _("Nüsschen")),
    ("sam", _("Sammelbalgfrucht")),
    ("soe", _("Schötchen")),
    ("smf", _("Schote mit falscher Scheidewand")),
    ("sos", _("Schote ohne Scheidewand")),
    ("spa", _("Spaltfrucht")),
    ("ste", _("Steinfrucht")),
    ("stc", _("Steinfrüchtchen")),
)
# ovule --------------------------------------------------------------------------------
OVULE_POSITION_CHOICES = (
    ("fr", _("Fruchtknoten (Angiospermen)")),
    ("za", _("Zapfenschuppe (Gymnospermen)")),
)
# --------------------------------------------------------------------------------------


# StemRoot choices ---------------------------------------------------------------------
# stem_morphology ----------------------------------------------------------------------
STEM_GROWTH_ORIENTATION_CHOICES = (
    ("abs", _("abstehend")),
    ("auf", _("aufrecht")),
    ("aua", _("aufrecht-abstehend")),
    ("aus", _("aufsteigend/aufstrebend")),
    ("flu", _("flutend")),
    ("gek", _("gekniet")),
    ("hae", _("hängend")),
    ("hor", _("horstig")),
    ("kri", _("kriechend")),
    ("lie", _("liegend")),
    ("loc", _("lockerrasig")),
    ("nic", _("nickend")),
    ("ran", _("rankenpflanzen")),
    ("spa", _("sparrig")),
    ("spr", _("spreizklimmig")),
    ("ueb", _("übergebogen")),
    ("win", _("windepflanzen")),
    ("wur", _("wurzelkletternd")),
    ("zur", _("zurückgeschlagen")),
)
STEM_APPEARANCE_CHOICES = (("k", _("krautig")), ("h", _("holzig")))
SR_STEM_SUCCULENCE_CHOICES = SUCCULENCE_CHOICES
SR_STEM_PITH_CHOICES = (("h", _("hohl")), ("m", _("markig")))
SR_STEM_CROSS_SECTION_CHOICES = (
    ("gfl", _("geflügelt")),
    ("gef", _("gefurcht")),
    ("ger", _("gerieft/gerillt")),
    ("gri", _("gerippt")),
    ("hal", _("halbstielrund")),
    ("kan", _("kantig")),
    ("kgs", _("kantig gefurcht/scharfkantig")),
    ("kno", _("knotig")),
    ("sti", _("stielrund")),
    ("stu", _("stumpfkantig")),
    ("zus", _("zusammengedrückt")),
    ("zwe", _("zweischneidig")),
)
SR_STEM_SURFACE_CHOICES = SURFACE_CHOICES
# outgrowths ---------------------------------------------------------------------------
CREEP_LAY_SHOOTS_CHOICES = ((None, _("None")), (True, _("Ja")), (False, _("Nein")))
RUNNERS_CHOICES = ((None, _("None")), (True, _("Ja")), (False, _("Nein")))
# root_morphology ----------------------------------------------------------------------
ROOT_ORGANS_CHOICES = (
    ("Inn", _("Innovations-Wurzelknolle")),
    ("Rhi", _("Rhizom")),
    ("Aus", _("unterirdische Ausläufer")),
    ("Wur", _("Wurzeln")),
    ("Wuk", _("Wurzelknollen")),
    ("Zwi", _("Zwiebel")),
)
ROOT_PRIMARY_ROOT_CHOICES = (
    ("erh", _("erhalten")),
    ("ers", _("durch sprossbürtige Wurzeln ersetzt")),
)
# --------------------------------------------------------------------------------------


# StemRhizomePoales choices ------------------------------------------------------------
# growth_form --------------------------------------------------------------------------
TUFT_STOLON_CHOICES = (
    ("loH", _("lockerer Horst")),
    ("auH", _("ausgebreiteter Horst")),
    ("dfH", _("dichter, fester Horst")),
    ("obA", _("oberirdische Ausläufer (Stolone)")),
    ("unA", _("unterirdische Ausläufer (Rhizome)")),
)
TUFT_STOLON_EDIT_DICT = {
    "loH": _("lockerem Horst"),
    "auH": _("ausgebreitetem Horst"),
    "dfH": _("dichtem, festem Horst"),
    "obA": _("oberirdischen Ausläufern (Stolone)"),
    "unA": _("unterirdischen Ausläufern (Rhizome)"),
}
# stem ---------------------------------------------------------------------------------
STEM_HAIRINESS_CHOICES = (("g", _("glatt")), ("k", _("kahl")), ("b", _("behaart")))
STEM_CROSS_SECTION_CHOICES = (
    ("sti", _("stilrund")),
    ("fla", _("flachgedrückt")),
    ("std", _("stumpf dreikantig")),
    ("scd", _("scharf dreikantig")),
    ("dre", _("dreikantig")),
)
STEM_PITH_CHOICES = (
    ("h", _("hohl")),
    ("n", _("hohl; nur Knoten markig")),
    ("m", _("markig")),
)
STEM_NODES_CHOICES = (("m", _("mit Knoten")), ("o", _("ohne Knoten")))
STEM_NODES_HAIRINESS_CHOICES = (("k", _("kahl")), ("b", _("behaart")))
STEM_TRANSVERSE_WALLS_CHOICES = (("m", _("mit Querwänden")), ("o", _("ohne Querwände")))
STEM_SURFACE_CHOICES = (
    ("", "---------"),
    ("gla", _("glatt")),
    ("ung", _("ungerieft")),
    ("ger", _("gerieft")),
    ("lae", _("längsgerippt")),
    ("feg", _("fein gestreift")),
)
STEM_SURFACE_DICT = dict(STEM_SURFACE_CHOICES[1:])
# rhizome ------------------------------------------------------------------------------
RHIZOME_LENGTH_CHOICES = (("k", _("kurz")), ("m", _("mittellang")), ("l", _("lang")))
RHIZOME_BRANCHING_CHOICES = (("g", _("gering verzweigt")), ("s", _("stark verzweigt")))
# --------------------------------------------------------------------------------------


# Indicators choices -------------------------------------------------------------------
LIGHT_CHOICES = (
    ("L1", _("L1 – Tiefschattenpflanze")),
    ("L2", _("L2 – zwischen Tiefschatten- und Schattenpflanze")),
    ("L3", _("L3 – Schattenpflanze")),
    ("L4", _("L4 – zwischen Schatten- und Halbschattenpflanze")),
    ("L5", _("L5 – Halbschattenpflanze")),
    ("L6", _("L6 – zwischen Halbschatten- und Halblichtpflanze")),
    ("L7", _("L7 – Halblichtpflanze")),
    ("L8", _("L8 – Lichtpflanze")),
    ("L9", _("L9 – Vollichtpflanze")),
    ("Lx", _("Lx – indifferentes Vehalten")),
    ("L?", _("L? – ungeklärtes Verhalten")),
)
TEMPERATURE_CHOICES = (
    ("T1", _("T1 – Kältezeiger")),
    ("T2", _("T2 – zwischen Kälte- und Kühlezeiger")),
    ("T3", _("T3 – Kühlezeiger")),
    ("T4", _("T4 – zwischen Kühle- und Mäßigwärmezeiger")),
    ("T5", _("T5 – Mäßigwärmezeiger")),
    ("T6", _("T6 – zwischen Mäßigwärme- und Wärmezeiger")),
    ("T7", _("T7 – Wärmezeiger")),
    ("T8", _("T8 – zwischen Wärme- und extremer Wärmezeiger")),
    ("T9", _("T9 – extremer Wärmezeiger")),
    ("Tx", _("Tx – indifferentes Verhalten")),
    ("T?", _("T? – ungeklärtes Verhalten")),
)
HUMIDITY_CHOICES = (
    ("F1", _("F1 – Starktrockniszeiger")),
    ("F2", _("F2 – zwischen Starktrocknis- und Trockniszeiger")),
    ("F3", _("F3 – Trockniszeiger")),
    ("F4", _("F4 – zwischen Trocknis- und Frischezeiger")),
    ("F5", _("F5 – Frischezeiger")),
    ("F6", _("F6 – zwischen Frische- und Feuchtezeiger")),
    ("F7", _("F7 – Feuchtezeiger")),
    ("F8", _("F8 – zwischen Feuchte- und Nässezeiger")),
    ("F9", _("F9 – Nässezeiger")),
    ("F10", _("F10 – Wechselwasserzeiger")),
    ("F11", _("F11 – Wasserpflanze")),
    ("F12", _("F12 – Unterwasserpflanze")),
    ("Fx", _("Fx – indifferentes Verhalten")),
    ("F?", _("F? – ungeklärtes Verhalten")),
)
REACTION_CHOICES = (
    ("R1", _("R1 – Starksäurezeiger")),
    ("R2", _("R2 – zwischen Starksäure- und Säurezeiger")),
    ("R3", _("R3 – Säurezeiger")),
    ("R4", _("R4 – zwischen Säure- und Mäßigsäurezeiger")),
    ("R5", _("R5 – Mäßigsäurezeiger")),
    (
        "R6",
        _("R6 – zwischen Mäßigsäurezeiger und Schwachsäure- bis Schwachbasenzeiger"),
    ),
    ("R7", _("R7 – Schwachsäure- bis Schwachbasenzeiger")),
    (
        "R8",
        _("R8 – zwischen Schwachsäure- bis Schwachbasen- und Basen- und Kalkzeiger"),
    ),
    ("R9", _("R9 – Basen- und Kalkzeiger")),
    ("Rx", _("Rx – indifferentes Verhalten")),
    ("R?", _("R? – ungeklärtes Verhalten")),
)
NITROGEN_CHOICES = (
    ("N1", _("N1 – stickstoffärmste Standorte")),
    ("N2", _("N2 – zwischen stickstoffärmste und -arme Standorte")),
    ("N3", _("N3 – stickstoffarme häufiger als mäßig -reiche Standorte")),
    ("N4", _("N4 – mäßig stickstoffreiche häufiger als -arme Standorte")),
    ("N5", _("N5 – mäßig stickstoffreiche Standorte")),
    ("N6", _("N6 – mäßig stickstoffreiche häufiger als -reiche Standorte")),
    ("N7", _("N7 – stickstoffreiche haufiger als mäßig -reiche Standorte")),
    ("N8", _("N8 – zwischen stickstoffreiche und übermäßig -reiche Standorte")),
    ("N9", _("N9 – übermäßig stickstoffreiche Standorte")),
    ("Nx", _("Nx – indifferentes Verhalten")),
    ("N?", _("N? – ungeklärtes Verhalten")),
)
KEY_CHOICES = (
    ("( )", _("( ) Keimlingsangabe")),
    ("(?)", _("(?) unsichere Einstufung")),
    ("~", _("~ Zeiger für starken Wechsel")),
    ("=", _("= Überschwemmungszeiger")),
)
# Generate dictionary with indicators as keys and dictionaries as values, with the
# dictionaries having indicator values as keys and verbose descriptions as values.
INDICATORS = ("light", "temperature", "humidity", "reaction", "nitrogen")
INDICATORS_CHOICES = (
    LIGHT_CHOICES,
    TEMPERATURE_CHOICES,
    HUMIDITY_CHOICES,
    REACTION_CHOICES,
    NITROGEN_CHOICES,
)
INDICATORS_DICT = dict(
    zip(
        INDICATORS,
        (dict((x, y.split(" – ")[-1]) for x, y in z) for z in INDICATORS_CHOICES),
    )
)
# --------------------------------------------------------------------------------------


# InterestingFacts Choices -------------------------------------------------------------
POLLINATION_CHOICES = (
    ("Ins", _("Insektenbestäubung")),
    ("Sel", _("Selbstbestäubung")),
    ("Was", _("Wasserbestäubung")),
    ("Win", _("Windbestäubung")),
)
DISPERSAL_CHOICES = (
    ("Men", _("Menschenausbreitung")),
    ("Sel", _("Selbstausbreitung")),
    ("Sto", _("Stoß-/Schüttelausbreitung")),
    ("Ved", _("Verdauungsausbreitung")),
    ("Ves", _("Versteck- u. Verlustausbreitung")),
    ("Was", _("Wasserausbreitung")),
    ("Win", _("Windausbreitung")),
)
# --------------------------------------------------------------------------------------
