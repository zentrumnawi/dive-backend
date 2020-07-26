from django.utils.translation import ugettext_lazy as _


NERV_CHOICES = (
    ("str", _("streifennervig")),
    ("net", _("netznervig")),
    ("fie", _("fiedernervig")),
    ("fin", _("fingernervig")),
    ("fus", _("fußnervig")),
    ("gab", _("gabelnervig")),
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
    ("hin", _("hinfällig")),
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
    ("ges", _("gescheitelt")),
)
SPR_WHOLE_CHOICES = (("ein", _("einfach")), ("zus", _("zusammengesetzt")))
SPR_STRUCTURE_CHOICES = (("ei", _("Einschnitte")), ("bl", _("Blättchen")))
CUT_CHOICES = (
    ("gan", _("ganz/ungeteilt")),
    ("gel", _("gelappt")),
    ("gep", _("gespalten")),
    ("get", _("geteilt")),
    ("ges", _("geschnitten")),
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
    ("fuz", _("fußförmig zusammengesetzt")),
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
    ("sil", _("schildförmig")),
)
LEAFLET_CHOICES = (
    (("dor"), _("dornig")),
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
    ("rra", _("rückwärts rauh")),
)
TEXTURE_CHOICES = (
    ("kra", _("krautig")),
    ("fle", _("fleischig")),
    ("led", _("lederig")),
    ("hae", _("häutig/trockenhäutig")),
    ("imm", _("immergrün")),
    ("sta", _("starr/steif")),
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
    ("nac", _("nackt")),
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
    ("rur", _("rückwärts rauh")),
)
DIAM_CHOICES = (
    ("zur", _("zurückgerollt/umgerollt")),
    ("ein", _("eingerollt")),
    ("zus", _("zusammengerollt")),
    ("gef", _("gefalzt/gefaltet")),
    ("rin", _("rinnig")),
    ("gek", _("gekielt")),
    ("dop", _("doppelrillig")),
)
SP_CHOICES = (
    ("kei", _("keilig/keilförmig")),
    ("ver", _("verschmälert")),
    ("abg", _("abgerundet")),
    ("ges", _("gestutzt")),
    ("her", _("herzförmig")),
    ("nie", _("nierenförmig")),
    ("pfe", _("pfeilförmig")),
    ("spi", _("spießförmig")),
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
SPREAD_CHOICES = (("sa", _("Samen")), ("sp", _("Sporen")))
FRUIT_POS_CHOICES = (
    ("fr", _("Fruchtknoten")),
    ("za", _("Zapfenschuppe")),
    ("sp", _("Sprossachse")),
)
TYPE_CHOICES = (
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
    ("non", _("nicht vorhanden"))
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
YES_NO_CHOICES = (
    ("yes", _("ja")),
    ("no", _("nein"))
)
GRIFFEL_SUB_CHOICES = (
    ("end", _("subendständig")),
    ("sei", _("subseitenständig")),
    ("gru", _("subgrundständig")),
    ("gyn", _("subgynobasisch"))
)
