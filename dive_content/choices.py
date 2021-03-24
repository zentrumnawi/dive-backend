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
    (("kei"), _("keine Grundblattrosette")),
)
BLADE_SUBDIV_SHAPE_CHOICES = (
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
INCISION_DEPTH_CHOICES = (
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
LEAFLET_INCISION_DEPTH_CHOICES = INCISION_DEPTH_CHOICES
BLADE_UNDIV_SHAPE_CHOICES = (
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
    ("vor", _("vorwärts rauh")),
    ("rur", _("rückwärts rauh")),
)
SURFACE_CHOICES = (
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

BL_TYPE_CHOICES = (
    ("ein", _("einzeln")),
    ("tra", _("Traube")),
    ("ris", _("Rispe")),
    ("ebe", _("Ebenstrauß/Corymbus")),
    ("sct", _("Schirmtraube")),
    ("scr", _("Schirmrispe")),
    ("spi", _("Spirre/Trichterrispe")),
    ("aer", _("Ähre")),
    ("kol", _("Kolben")),
    ("kae", _("Kätzchen")),
    ("zap", _("Zapfen")),
    ("dol", _("Dolde")),
    ("dod", _("Doppeldolde")),
    ("kop", _("Kopf")),
    ("koc", _("Köpfchen")),
    ("kor", _("Korb")),
    ("krc", _("Körbchen")),
    ("zym", _("Zyme")),
    ("ple", _("Pleiochasium")),
    ("dic", _("Dichasium")),
    ("mon", _("Monochasium")),
    ("wic", _("Wickel")),
    ("dow", _("Doppelwickel")),
    ("scq", _("Scheinquirl")),
    ("bue", _("Büschel")),
    ("kna", _("Knäuel")),
    ("thy", _("Thyrse")),
    ("scd", _("Scheindolde/Trugdolde")),
    ("scb", _("Scheinblüte/Pseudanthium")),
)
SYM_CHOICES = (
    ("r", _("radiärsymmetrisch/aktinomorph/strahlig")),
    ("d", _("disymmetrisch/bilateral")),
    ("z", _("zygomorph/dorsiventral")),
    ("a", _("asymmetrisch/unregelmäßig")),
)
PART_CHOICES = (
    ("gan", _("ganz/ungeteilt")),
    ("gel", _("gelappt")),
    ("gsp", _("gespalten")),
    ("get", _("geteilt")),
    ("ges", _("geschnitten")),
    ("han", _("handförmig/fingerförmig")),
    ("hgl", _("handförmig gelappt")),
    ("hgt", _("handförmig geteilt")),
    ("hgs", _("handförmig geschnitten")),
    ("gef", _("gefingert")),
    ("fie", _("fiederförmig/fiederig")),
    ("fil", _("fiederlappig")),
    ("fsp", _("fiederspaltig")),
    ("fit", _("fiederteilig")),
    ("fis", _("fiederschnittig")),
    ("paf", _("paarig gefiedert")),
    ("upf", _("unpaarig gefiedert")),
    ("unf", _("unterbrochen fiederschnittig")),
    ("ung", _("unterbrochen gefiedert")),
    ("dop", _("doppelt gefiedert")),
    ("meh", _("mehrfach gefiedert")),
    ("dre", _("dreizählig")),
    ("dod", _("doppelt dreizählig")),
    ("lei", _("leierförmig")),
    ("sch", _("schrotsägeförmig")),
    ("kam", _("kammförmig")),
    ("fug", _("fußförmig geschnitten")),
    ("fuz", _("fußförmig zusammengesetzt")),
    ("non", _("nicht vorhanden")),
)
HULL_CHOICES = (
    ("dop", _("doppelte Blütenhülle (Kalyx + Corolla)")),
    ("ein", _("einfache Blütenhülle (Perigon)")),
    ("feh", _("fehlende Blütenhülle")),
    ("lip", _("Lippenblüte")),
    ("sch", _("Schmetterlingsblüte")),
    ("zun", _("Zungenblüte")),
    ("str", _("strahlende Randblüten")),
)
CH_TYPE_CHOICES = (
    ("fre", _("freiblättrig")),
    ("ver", _("verwachsenblättrig")),
    ("2-z", _("2-zähnig")),
    ("3-z", _("3-zähnig")),
    ("4-z", _("4-zähnig")),
    ("5-z", _("5-zähnig")),
    ("2-l", _("2-lappig")),
    ("3-l", _("3-lappig")),
    ("4-l", _("4-lappig")),
    ("5-l", _("5-lappig")),
    ("2-s", _("2-spaltig")),
    ("3-s", _("3-spaltig")),
    ("4-s", _("4-spaltig")),
    ("5-s", _("5-spaltig")),
    ("2-t", _("2-teilig")),
    ("3-t", _("3-teilig")),
    ("4-t", _("4-teilig")),
    ("5-t", _("5-teilig")),
    ("zwe", _("zweilippig")),
)
CROWN_VER_CHOICES = (
    ("v", _("verwachsen")),
    ("u", _("unverwachsen")),
    ("a", _("am Grund verwachsen")),
)
STAND_TYPE_CHOICES = (
    ("hy", _("hypogyn/oberständig")),
    ("eh", _("epihypogyn/halboberständig")),
    ("pe", _("perigyn/mittelständig")),
    ("he", _("hemiepigyn/halbunterständig")),
    ("ep", _("epigyn/unterständig")),
)
BUILD_CHOICES = (
    ("mo", _("monokarp")),
    ("ap", _("apokarp/chorikarp")),
    ("cs", _("coeno-synkarp")),
    ("cp", _("coeno-parakarp")),
)
GRIFFEL_CHOICES = (
    ("en", _("endständig")),
    ("se", _("seitenständig")),
    ("gr", _("grundständig")),
    ("gy", _("gynobasisch")),
)
GRIFFEL_SUB_CHOICES = (
    ("end", _("subendständig")),
    ("sei", _("subseitenständig")),
    ("gru", _("subgrundständig")),
    ("gyn", _("subgynobasisch")),
)
SPEC_SPORN_CHOICES = (
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
    ("loc", _("lockerrasig")),
)
APPEARANCE_CHOICES = (("k", _("krautig")), ("h", _("holzig")))
YES_NO_CHOICES = (("yes", _("ja")), ("no", _("nein")))
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
    ("kno", _("knotig")),
)
# SURFACE_CHOICES  =>  Leaf choices
SUR_TEXTURE_CHOICES = SURFACE_CHOICES
CREEP_LAY_SHOOTS_CHOICES = (
    ("bil", _("bildet Kriech- und Legetriebe")),
    ("kei", _("keine Angabe")),
)
RUNNERS_CHOICES = (
    ("bil", _("bildet oberirdische Ausläufer")),
    ("kei", _("keine Angabe")),
)
ORGANS_CHOICES = (
    ("Rhi", _("Rhizom")),
    ("Zwi", _("Zwiebel")),
    ("Aus", _("unterirdische Ausläufer")),
    ("Inn", _("Innovations-Wurzelknolle")),
    ("Wuk", _("Wurzelknollen")),
    ("Wur", _("Wurzeln")),
)
ROOT_CHOICES = (
    ("erh", _("erhalten")),
    ("ers", _("ersetzt durch sprossbürtige Wurzeln")),
)


# ZeigerNumber Choices

LIGHT_CHOICES = (
    ("L1 - Tiefschattenpflanze", "L1 - Tiefschattenpflanze"),
    (
        "L2 - zwischen Tiefschatten- und Schattenpflanze",
        "L2 - zwischen Tiefschatten- und Schattenpflanze",
    ),
    ("L3 - Schattenpflanze", "L3 - Schattenpflanze"),
    (
        "L4 - zwischen Schatten- und Halbschattenpflanze",
        "L4 - zwischen Schatten- und Halbschattenpflanze",
    ),
    ("L5 - Halbschattenpflanze", "L5 - Halbschattenpflanze"),
    (
        "L6 - zwischen Halbschatten- und Halblichtpflanze",
        "L6 - zwischen Halbschatten- und Halblichtpflanze",
    ),
    ("L7 - Halblichtpflanze", "L7 - Halblichtpflanze"),
    ("L8 - Lichtpflanze", "L8 - Lichtpflanze"),
    ("L9 - Vollichtpflanze", "L9 - Vollichtpflanze"),
    ("Lx - indifferentes Verhalten", "Lx - indifferentes Verhalten"),
    ("L? - ungeklärtes Verhalten", "L? - ungeklärtes Verhalten"),
    ("nicht angegeben", "nicht angegeben"),
)
TEMP_CHOICES = (
    ("T1 - Kältezeiger", "T1 - Kältezeiger"),
    ("T2 - zwischen Kälte- und Kühlezeiger", "T2 - zwischen Kälte- und Kühlezeiger"),
    ("T3 - Kühlezeiger", "T3 - Kühlezeiger"),
    (
        "T4 - zwischen Kühle- und Mäßigwärmezeiger",
        "T4 - zwischen Kühle- und Mäßigwärmezeiger",
    ),
    ("T5 - Mäßigwärmezeiger", "T5 - Mäßigwärmezeiger"),
    (
        "T6 - zwischen Mäßigwärme- und Wärmezeiger",
        "T6 - zwischen Mäßigwärme- und Wärmezeiger",
    ),
    ("T7 - Wärmezeiger", "T7 - Wärmezeiger"),
    (
        "T8 - zwischen Wärme- und extremer Wärmezeiger",
        "T8 - zwischen Wärme- und extremer Wärmezeiger",
    ),
    ("T9 - extremer Wärmezeiger", "T9 - extremer Wärmezeiger"),
    ("Tx - indifferentes Verhalten", "Tx - indifferentes Verhalten"),
    ("T? - ungeklärtes Verhalten", "T? - ungeklärtes Verhalten"),
    ("nicht angegeben", "nicht angegeben"),
)
HUMID_CHOICES = (
    ("F1 - Starktrockniszeiger", "F1 - Starktrockniszeiger"),
    (
        "F2 - zwischen Starktrocknis- und Trockniszeiger",
        "F2 - zwischen Starktrocknis- und Trockniszeiger",
    ),
    ("F3 - Trockniszeiger", "F3 - Trockniszeiger"),
    (
        "F4 - zwischen Trocknis- und Frischezeiger",
        "F4 - zwischen Trocknis- und Frischezeiger",
    ),
    ("F5 - Frischezeiger", "F5 - Frischezeiger"),
    (
        "F6 - zwischen Frische- und Feuchtezeiger",
        "F6 - zwischen Frische- und Feuchtezeiger",
    ),
    ("F7 - Feuchtezeiger", "F7 - Feuchtezeiger"),
    (
        "F8 - zwischen Feuchte- und Nässezeiger",
        "F8 - zwischen Feuchte- und Nässezeiger",
    ),
    ("F9 - Nässezeiger", "F9 - Nässezeiger"),
    ("F10 - Wechselwasserzeiger", "F10 - Wechselwasserzeiger"),
    ("F11 - Wasserpflanze", "F11 - Wasserpflanze"),
    ("F12 - Unterwasserpflanze", "F12 - Unterwasserpflanze"),
    ("Fx - indifferentes Verhalten", "Fx - indifferentes Verhalten"),
    ("F? - ungeklärtes Verhalten", "F? - ungeklärtes Verhalten"),
    ("F= - Überschwemmungszeiger", "F= - Überschwemmungszeiger"),
    ("nicht angegeben", "nicht angegeben"),
)
REACT_CHOICES = (
    ("R1 - Starksäurezeiger", "R1 - Starksäurezeiger"),
    (
        "R2 - zwischen Starksäure- und Säurezeiger",
        "R2 - zwischen Starksäure- und Säurezeiger",
    ),
    ("R3 - Säurezeiger", "R3 - Säurezeiger"),
    (
        "R4 - zwischen Säure- und Mäßigsäurezeiger",
        "R4 - zwischen Säure- und Mäßigsäurezeiger",
    ),
    ("R5 - Mäßigsäurezeiger", "R5 - Mäßigsäurezeiger"),
    (
        "R6 - zwischen Mäßigsäurezeiger und Schwachsäure- bis Schwachbasenzeiger",
        "R6 - zwischen Mäßigsäurezeiger und Schwachsäure- bis Schwachbasenzeiger",
    ),
    (
        "R7 - Schwachsäure- bis Schwachbasenzeiger",
        " R7 - Schwachsäure- bis Schwachbasenzeiger",
    ),
    (
        "R8 - zwischen Schwachsäure- bis Schwachbasen- und Basen- und Kalkzeiger",
        "R8 - zwischen Schwachsäure- bis Schwachbasen- und Basen- und Kalkzeiger",
    ),
    ("R9 - Basen- und Kalkzeiger", "R9 - Basen- und Kalkzeiger"),
    ("Rx - indifferentes Verhalten", "Rx - indifferentes Verhalten"),
    ("R? - ungeklärtes Verhalten", "R? - ungeklärtes Verhalten"),
    ("nicht angegeben", "nicht angegeben"),
)
NUTRIENT_CHOICES = (
    (
        "N1 - stickstoffärmste Stanorte anzeigend",
        "N1 - stickstoffärmste Stanorte anzeigend",
    ),
    (
        "N2 - zwischen stickstoffärmsten und -armen Standorten",
        "N2 - zwischen stickstoffärmsten und -armen Standorten",
    ),
    (
        "N3 - häufig auf stickstoffarmen Standorten",
        "N3 - häufig auf stickstoffarmen Standorten",
    ),
    (
        "N4 - zwischen: häufig auf stickstoffarmen und mäßig -reichen Standorten",
        "N4 - zwischen: häufig auf stickstoffarmen und mäßig -reichen Standorten",
    ),
    ("N5 - mäßig stickstoffreiche Standorte", "N5 - mäßig stickstoffreiche Standorte"),
    (
        "N6 - zwischen: mäßig und häufig anstickstoffreichen Standorten",
        "N6 - zwischen: mäßig und häufig anstickstoffreichen Standorten",
    ),
    (
        "N7 - häufig an stickstoffreichen Standorten",
        "N7 - häufig an stickstoffreichen Standorten",
    ),
    (
        "N8 - zwischen: häufig an und übermäßig stickstoffreichen Stanorten",
        "N8 - zwischen: häufig an und übermäßig stickstoffreichen Stanorten",
    ),
    (
        "N9 - übermäßig stickstoffreiche Standorte",
        "N9 - übermäßig stickstoffreiche Standorte",
    ),
    ("Nx - indifferentes Verhalten", "Nx - indifferentes Verhalten"),
    ("N? - ungeklärtes Verhalten", "N? - ungeklärtes Verhalten"),
    ("nicht angegeben", "nicht angegeben"),
)
ZEIGER_EXTRA = (("~", "~"), ("(?)", "(?)"))
