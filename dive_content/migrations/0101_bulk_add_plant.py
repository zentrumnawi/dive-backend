# Generated by Django 3.0.8 on 2021-12-13 12:38

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0100_rename_plant_ground"),
    ]

    operations = [
        migrations.AddField(
            model_name="plant",
            name="alternative_trivial_names",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=50),
                blank=True,
                default=list,
                size=4,
                verbose_name="Alternative Trivialnamen",
            ),
        ),
        migrations.AddField(
            model_name="plant",
            name="ground",
            field=models.PositiveSmallIntegerField(
                blank=True,
                choices=[
                    (1, "kalkfrei, basisch"),
                    (2, "kalkarm"),
                    (3, "feucht, zum Teil periodisch überschwemmt"),
                    (4, "frisch bis feucht, meist nährstoffreich"),
                    (5, "frisch und nährstoffreich"),
                    (6, "lehmig bis tonig"),
                    (7, "mäßig nährstoffreich"),
                    (8, "nährstoff(stickstoff)reich"),
                    (9, "nährstoffreich"),
                ],
                null=True,
                verbose_name="Untergrund",
            ),
        ),
        migrations.AddField(
            model_name="plant",
            name="habitats",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.PositiveSmallIntegerField(
                    choices=[
                        (300, "Äcker"),
                        (200, "Ansaaten"),
                        (201, "Auengebüsche"),
                        (100, "Auengebüschsäume"),
                        (202, "Auenwälder"),
                        (101, "Auenwaldsäume"),
                        (102, "Bäche"),
                        (103, "Bachränder"),
                        (301, "Bahnanlagen"),
                        (302, "Brachen"),
                        (203, "Bruchwälder"),
                        (204, "Buchenwälder"),
                        (303, "Dämme"),
                        (205, "Eichen-Hainbuchen-Wälder"),
                        (206, "Ephemerenfluren"),
                        (207, "Erlenwälder"),
                        (104, "Felsen"),
                        (304, "Fettwiesen"),
                        (208, "Flussuferstaudenfluren"),
                        (209, "Forste"),
                        (305, "Friedhöfe"),
                        (306, "Frischwiesen"),
                        (210, "Gärten"),
                        (211, "Gebüsche"),
                        (212, "Gebüschsäume"),
                        (213, "Gräben"),
                        (105, "Grabenränder"),
                        (307, "Grünlandbrachen"),
                        (214, "Hackkulturen"),
                        (308, "Halbtrockenrasen"),
                        (106, "Hänge"),
                        (215, "Hangwälder"),
                        (216, "Hecken"),
                        (107, "Heckenränder"),
                        (217, "Heiden"),
                        (218, "Hochgrasfluren"),
                        (219, "Hochstaudenfluren"),
                        (309, "Intensivgrünländer"),
                        (220, "Kalkfelsenfluren"),
                        (310, "Kalktrockenrasen"),
                        (221, "Kiesgruben"),
                        (311, "Kleeäcker"),
                        (222, "Laubmischwälder"),
                        (108, "Laubmischwaldsäume"),
                        (223, "Laubwälder"),
                        (312, "Magerrasen"),
                        (313, "Magerweiden"),
                        (109, "Mauern"),
                        (224, "Mischwälder"),
                        (225, "Moorwälder"),
                        (226, "Nadelholzforste"),
                        (227, "Nadelwälder"),
                        (314, "Obstwiesen"),
                        (228, "Parkanlagen"),
                        (315, "Parkrasen"),
                        (229, "Parks"),
                        (230, "Pioniergehölze"),
                        (110, "Quellen"),
                        (231, "Quellmoore"),
                        (316, "Rasen"),
                        (232, "Rasenansaaten"),
                        (233, "Robinienforste"),
                        (234, "Röhrichte"),
                        (317, "Ruderalflächen"),
                        (318, "Sandtrockenrasen (Küstendünen)"),
                        (111, "Säume"),
                        (235, "Schläge"),
                        (236, "Schlaggehölze"),
                        (237, "Schlammfluren"),
                        (238, "Schluchtwälder"),
                        (319, "Schutt"),
                        (320, "Schutthalden"),
                        (321, "Silikatmagerrasen"),
                        (239, "Staudenfluren"),
                        (240, "Steinbrüche"),
                        (322, "Steinriegel"),
                        (241, "Steinschuttfluren"),
                        (323, "Sumpfwiesen"),
                        (112, "Talhänge"),
                        (324, "Trittrasen"),
                        (325, "Trittstellen"),
                        (113, "Trockengebüschsäume"),
                        (326, "Trockenrasen"),
                        (114, "Trockenwaldsäume"),
                        (115, "Ufer"),
                        (242, "Uferstaudenfluren"),
                        (327, "Verlichtungen"),
                        (328, "Viehläger"),
                        (243, "Vorwälder"),
                        (244, "Vorwaldgehölze"),
                        (245, "Wälder"),
                        (329, "Waldlichtungen"),
                        (116, "Waldquellen"),
                        (117, "Waldränder"),
                        (118, "Waldsäume"),
                        (246, "Waldschläge"),
                        (247, "Waldverlichtungen"),
                        (330, "Waldwege"),
                        (119, "Waldwegränder"),
                        (120, "Wegränder"),
                        (331, "Weiden"),
                        (248, "Weinberge"),
                        (332, "Wiesen"),
                        (333, "Xerothermrasen"),
                    ]
                ),
                blank=True,
                default=list,
                size=None,
                verbose_name="Habitate",
            ),
        ),
        migrations.AddField(
            model_name="plant",
            name="ruderal_sites",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.PositiveSmallIntegerField(
                    choices=[
                        (1, "Bahnanlagen"),
                        (2, "Bahndämme"),
                        (3, "Böschungen"),
                        (4, "Bruchwälder"),
                        (5, "Dämme"),
                        (6, "Geröllstände"),
                        (7, "Gleitschotter"),
                        (8, "Gräben"),
                        (9, "Kiesgruben"),
                        (10, "an Mauern"),
                        (11, "Pflasterfugen"),
                        (12, "Schutt"),
                        (13, "Steinbrüche"),
                        (14, "Straßenböschungen"),
                        (15, "Tagebaue"),
                        (16, "Trittstellen"),
                        (17, "Waldränder"),
                        (18, "Waldschläge"),
                        (19, "Wegränder"),
                        (20, "Xerothermrasen"),
                        (21, "an Zäunen"),
                    ]
                ),
                blank=True,
                default=list,
                size=None,
                verbose_name="Ruderalstandorte",
            ),
        ),
    ]