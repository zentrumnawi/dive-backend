from django.utils.translation import ugettext_lazy as _

# Leaf choices

VEINS_CHOICES = (
    ("str", _("streifennervig")),
    ("net", _("netznervig")),
    ("fie", _("fiedernervig")),
    ("fin", _("fingernervig")),
    ("fus", _("fußnervig")),
    ("gab", _("gabelnervig")),
)
DIVISION_CHOICES = (("ein", _("einfach")), ("zus", _("zusammengesetzt")))
SUCCULENCE_CHOICES = (("dic", _("dickfleischig")), (("ndi"), _("nicht dickfleischig")))
TEXTURE_CHOICES = (
    ("kra", _("krautig")),
    ("fle", _("fleischig")),
    ("led", _("lederig")),
    ("hae", _("häutig/trockenhäutig")),
    ("imm", _("immergrün")),
    ("sta", _("starr/steif")),
)
CROSS_SECTION_CHOICES = (
    ("zur", _("zurückgerollt/umgerollt")),
    ("ein", _("eingerollt")),
    ("zus", _("zusammengerollt")),
    ("gef", _("gefalzt/gefaltet")),
    ("rin", _("rinnig")),
    ("gek", _("gekielt")),
    ("dop", _("doppelrillig")),
)
ATTACHMENT_CHOICES = (
    ("ges", _("gestielt")),
    ("sit", _("sitzend/ungestielt")),
    ("ste", _("stengelumfassend")),
    ("hal", _("halbstengelumfassend")),
    ("dur", _("durchwachsen")),
    ("ver", _("verwachsen")),
    ("sch", _("scheidig verwachsen")),
    ("her", _("herablaufend")),
    ("rei", _("reitend")),
    ("hin", _("hinfällig")),
)
ARRANGMENT_CHOICES = (
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
    ("ges", _("gescheitelt")),
)
ROSETTE_CHOICES = (
    ("vor", _("Grundblattrossette vorhanden")),
    ("kei", _("keine Grundblattrosette")),
)
LEAF_COMP_BLADE_SHAPE_CHOICES = (
    ("han", _("handförmig")),
    ("gef", _("gefingert")),
    ("fif", _("fiederförmig")),
    ("fil", _("fiederlappig")),
    ("fip", _("fiederspaltig")),
    ("fit", _("fiederteilig")),
    ("fis", _("fiederschnittig")),
    ("paa", _("paarig")),
    ("unp", _("unpaarig")),
    ("unt", _("unterbrochen")),
    ("dop", _("doppelt")),
    ("meh", _("mehrfach")),
    ("dre", _("dreizählig")),
    ("dod", _("doppelt dreizählig")),
    ("lei", _("leierförmig")),
    ("sch", _("schrotsägeförmig")),
    ("kam", _("kammförmig")),
    ("fus", _("fußförmig")),
)
LEAF_COMP_INCISION_DEPTH_CHOICES = (
    ("gan", _("ganz/ungeteilt")),
    ("gel", _("gelappt")),
    ("gep", _("gespalten")),
    ("get", _("geteilt")),
    ("ges", _("geschnitten")),
    ("gef", _("gefingert")),
    ("zus", _("zusammengesetzt")),
    ("fis", _("fiederschnittig")),
    ("fie", _("gefiedert")),
)
LEAFLET_INCISION_DEPTH_CHOICES = LEAF_COMP_INCISION_DEPTH_CHOICES
LEAF_SIMPLE_BLADE_SHAPE_CHOICES = (
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
    ("sil", _("schildförmig")),
)
LEAF_SIMPLE_INCISION_DEPTH_CHOICES = (
    ("gan", _("ganz/ungeteilt")),
    ("gel", _("gelappt")),
    ("gep", _("gespalten")),
    ("get", _("geteilt")),
    ("ges", _("geschnitten")),
)
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
    ("gla", _("glatt")),
    ("run", _("runzelig")),
    ("rau", _("rau")),
    ("vra", _("vorwärts rau")),
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
    ("nac", _("nackt")),
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


# Blossom choices

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
INFLORESCENCE_TYPE_CHOICES_1_3 = (
    ("kol", _("Kolben")),
    ("kae", _("Kätzchen")),
    ("zap", _("Zapfen")),
    ("koc", _("Köpfchen")),
    ("krc", _("Körbchen")),
    ("bue", _("Büschel")),
    ("kna", _("Knäuel")),
)
INFLORESCENCE_TYPE_CHOICES_2_3 = (
    ("ein", _("Einzelblüte")),
    ("tra", _("Traube")),
    ("ris", _("Rispe")),
    ("sct", _("Schirmtraube")),
    ("scr", _("Schirmrispe")),
    ("spi", _("Spirre/Trichterrispe")),
    ("aer", _("Ähre")),
    ("dol", _("Dolde")),
    ("dod", _("Doppeldolde")),
    ("zym", _("Zyme")),
    ("wic", _("Wickel")),
    ("dow", _("Doppelwickel")),
    ("thy", _("Thyrse")),
    ("scd", _("Scheindolde/Trugdolde")),
)
INFLORESCENCE_TYPE_CHOICES_3_3 = (
    ("ebe", _("Ebenstrauß/Corymbus")),
    ("kop", _("Kopf")),
    ("kor", _("Korb")),
    ("ple", _("Pleiochasium")),
    ("dic", _("Dichasium")),
    ("mon", _("Monochasium")),
    ("scq", _("Scheinquirl")),
    ("scb", _("Scheinblüte/Pseudanthium")),
)
INFLORESCENCE_TYPE_CHOICES = (
    INFLORESCENCE_TYPE_CHOICES_1_3
    + INFLORESCENCE_TYPE_CHOICES_2_3
    + INFLORESCENCE_TYPE_CHOICES_3_3
)
INFLORESCENCE_TYPE_DICT_3_3_PLURAL = {
    "ebe": _("Ebensträuße/Corymbusse"),
    "kop": _("Köpfe"),
    "kor": _("Körbe"),
    "ple": _("Pleiochasien"),
    "dic": _("Dichasien"),
    "mon": _("Monochasien"),
    "scq": _("Scheinquirle"),
    "scb": _("Scheinblüten/Pseudanthien"),
}
MEROSITY_CHOICES = (
    ((None, "-"),) + tuple((x, x) for x in range(1, 9)) + ((9, _("viel")),)
)
SYMMETRY_CHOICES = (
    ("r", _("radiärsymmetrisch")),
    ("d", _("disymmetrisch")),
    ("z", _("zygomorph")),
    ("a", _("asymmetrisch")),
)
PERIANTH_CHOICES = (
    ("dop", _("doppelte Blütenhülle (Kalyx + Corolla)")),
    ("ein", _("einfache Blütenhülle (Perigon)")),
    ("feh", _("fehlende Blütenhülle")),
    ("lip", _("Lippenblüte")),
    ("sch", _("Schmetterlingsblüte")),
    ("zun", _("Zungenblüte")),
    ("roe", _("Röhrenblüte")),
    ("str", _("strahlende Randblüten")),
)
PERIANTH_FORM_CHOICES = (
    ("ro", _("röhrig")),
    ("ke", _("keulig")),
    ("gl", _("glockig")),
    ("tr", _("trichterförmig")),
    ("be", _("becherförmig")),
    ("na", _("napfförmig")),
    ("ku", _("kugelig")),
    ("au", _("aufgeblasen")),
    ("kr", _("krugförmig")),
    ("ra", _("radförmig")),
    ("st", _("stielförmig")),
    ("zu", _("zungenförmig")),
    ("ba", _("bauchig")),
    ("as", _("ausgesackt")),
    ("gr", _("gespornt")),
)
BRACT_BLADE_CHOICES = (
    LEAF_COMP_BLADE_SHAPE_CHOICES
    + LEAF_SIMPLE_BLADE_SHAPE_CHOICES
    + (("nvo", _("nicht vorhanden")),)
)
CONNATION_NUM_CHOICES = (("", "-"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"))
CONNATION_TYPE_CHOICES = (
    ("", "---------"),
    ("-z", _("-zähnig")),
    ("-l", _("-lappig")),
    ("-s", _("-spaltig")),
    ("-t", _("-teilig")),
    ("fre", _("freiblättrig")),
    ("ver", _("verwachsenblättrig")),
    ("zwe", _("zweilippig")),
)
SEPAL_CONNATION_CHOICES = (
    ("v", _("verwachsen")),
    ("u", _("unverwachsen")),
    ("a", _("am Grund verwachsen")),
)
PETAL_CONNATION_CHOICES = SEPAL_CONNATION_CHOICES
STAMEN_CONNATION_TYPE_CHOICES = (
    ("s", _("Staubfadenröhre")),
    ("v", _("verwachsen mit Kronblättern")),
)
CARPEL_CONNATION_TYPE_CHOICES = (
    ("mo", _("monokarp")),
    ("ap", _("apokarp/chorikarp")),
    ("cs", _("coeno-synkarp")),
    ("cp", _("coeno-parakarp")),
)
OVARY_POS_CHOICES = (
    ("ob", _("oberständig")),
    ("ho", _("halboberständig")),
    ("mi", _("mittelständig")),
    ("hu", _("halbunterständig")),
    ("un", _("unterständig")),
)
PISTIL_POS_CHOICES = (
    ("end", _("endständig")),
    ("sei", _("seitenständig")),
    ("gru", _("grundständig")),
    ("gyn", _("gynobasisch")),
    ("sen", _("subendständig")),
    ("sse", _("subseitenständig")),
    ("sgr", _("subgrundständig")),
    ("sgy", _("subgynobasisch")),
)
# ---------------------------------- TO BE MODIFIED ---------------------------------- #
GRANN_TOP_CHOICES = (("sp", _("Spitzengranne")), ("un", _("unbegrannt")))
GRANN_FORM_CHOICES = (("gr", _("gerade")), ("gk", _("gekniet")), ("gd", _("gedreht")))
GROUND_CHOICES = (
    ("ge", _("gestielt")),
    ("si", _("sitzend / ungestielt")),
    ("st", _("stengelumfassend")),
    ("ha", _("halbstengelumfassend")),
    ("du", _("durchwachsen")),
    ("ve", _("verwachsen")),
    ("sc", _("scheidig verwachsen")),
    ("he", _("herablaufend")),
    ("re", _("reitend")),
    ("hi", _("hinfällig")),
)
# ------------------------------------------------------------------------------------ #


# Fruit choices

FRUIT_TYPE_CHOICES = (
    ("apf", _("Apfelfrucht")),
    ("nus", _("Nuss")),
    ("kar", _("Karyopse")),
    ("ach", _("Achäne")),
    ("bee", _("Beere")),
    ("ste", _("Steinfrucht")),
    ("bal", _("Balgfrucht")),
    ("hue", _("Hülse")),
    ("kap", _("Kapsel")),
    ("sos", _("Schote ohne Scheidewand")),
    ("smf", _("Schote mit falscher Scheidewand")),
    ("soe", _("Schötchen")),
    ("spa", _("Spaltfrucht")),
    ("kok", _("Kokke")),
    ("dop", _("Doppelachäne")),
    ("bru", _("Bruchfrucht")),
    ("glh", _("Gliederhülse")),
    ("gls", _("Gliederschote")),
    ("kla", _("Klausenfrucht")),
    ("sam", _("Sammelbalgfrucht")),
    ("nue", _("Nüsschen")),
    ("stc", _("Steinfrüchtchen")),
    ("bac", _("Balgfrüchtchen")),
)
OVULE_POS_CHOICES = (
    ("fr", _("Fruchtknoten (Angiospermen)")),
    ("za", _("Zapfenschuppe (Gymnospermen)")),
)


# StemRoot choices

ORIENTATION_CHOICES = (
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
    ("hor", _("horstig")),
    ("loc", _("lockerrasig")),
    ("ran", _("rankenpflanzen")),
    ("win", _("windepflanzen")),
    ("spr", _("spreizklimmig")),
    ("wur", _("wurzelkletternd")),
)
APPEARANCE_CHOICES = (("k", _("krautig")), ("h", _("holzig")))
# SUCCULENCE_CHOICES  =>  Leaf choices
SR_CROSS_SECTION_CHOICES = (
    ("sti", _("stielrund")),
    ("hal", _("halbstielrund")),
    ("zus", _("zusammengedrückt")),
    ("zwe", _("zweischneidig")),
    ("kan", _("kantig")),
    ("stu", _("stumpfkantig")),
    ("ger", _("gerieft/gerillt")),
    ("gef", _("gefurcht")),
    ("kan", _("kantig gefurcht/scharfkantig")),
    ("gri", _("gerippt")),
    ("gfl", _("geflügelt")),
    ("kno", _("knotig")),
)
# SURFACE_CHOICES  =>  Leaf choices
CREEP_LAY_SHOOTS_CHOICES = (
    ("bil", _("bildet Kriech- und Legetriebe")),
    ("kei", _("keine Angabe")),
)
RUNNERS_CHOICES = (
    ("bil", _("bildet oberirdische Ausläufer")),
    ("kei", _("keine Angabe")),
)
BRACTS_CHOICES = (
    ("nur", _("nur am Grund")),
    ("auc", _("auch über dem Grund")),
)
ORGANS_CHOICES = (
    ("Rhi", _("Rhizom")),
    ("Zwi", _("Zwiebel")),
    ("Aus", _("unterirdische Ausläufer")),
    ("Inn", _("Innovations-Wurzelknolle")),
    ("Wuk", _("Wurzelknollen")),
    ("Wur", _("Wurzeln")),
)
PRIMARY_ROOT_CHOICES = (
    ("erh", _("erhalten")),
    ("ers", _("durch sprossbürtige Wurzeln ersetzt")),
)


# Indicators Choices

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
