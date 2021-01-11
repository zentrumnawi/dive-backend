# Generated by Django 3.0.8 on 2020-11-03 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0019_plant_facts_to_know"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plant",
            name="facts_to_know",
            field=models.TextField(
                default="", max_length=600, verbose_name="Wissenswertes"
            ),
        ),
        migrations.CreateModel(
            name="ZeigerNumber",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "light_number",
                    models.CharField(
                        blank=True,
                        choices=[
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
                            (
                                "Lx - indifferentes Verhalten",
                                "Lx - indifferentes Verhalten",
                            ),
                            (
                                "L? - ungeklärtes Verhalten",
                                "L? - ungeklärtes Verhalten",
                            ),
                            ("nicht angegeben", "nicht angegeben"),
                        ],
                        max_length=100,
                        null=True,
                        verbose_name="Lichtzahl",
                    ),
                ),
                (
                    "light_extra",
                    models.CharField(
                        blank=True,
                        choices=[("~", "~"), ("(?)", "(?)")],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "temp_number",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("T1 - Kältezeiger", "T1 - Kältezeiger"),
                            (
                                "T2 - zwischen Kälte- und Kühlezeiger",
                                "T2 - zwischen Kälte- und Kühlezeiger",
                            ),
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
                            (
                                "Tx - indifferentes Verhalten",
                                "Tx - indifferentes Verhalten",
                            ),
                            (
                                "T? - ungeklärtes Verhalten",
                                "T? - ungeklärtes Verhalten",
                            ),
                            ("nicht angegeben", "nicht angegeben"),
                        ],
                        max_length=100,
                        null=True,
                        verbose_name="Temperaturzahl",
                    ),
                ),
                (
                    "temp_extra",
                    models.CharField(
                        blank=True,
                        choices=[("~", "~"), ("(?)", "(?)")],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "humid_number",
                    models.CharField(
                        blank=True,
                        choices=[
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
                            (
                                "Fx - indifferentes Verhalten",
                                "Fx - indifferentes Verhalten",
                            ),
                            (
                                "F? - ungeklärtes Verhalten",
                                "F? - ungeklärtes Verhalten",
                            ),
                            (
                                "F= - Überschwemmungszeiger",
                                "F= - Überschwemmungszeiger",
                            ),
                            ("nicht angegeben", "nicht angegeben"),
                        ],
                        max_length=100,
                        null=True,
                        verbose_name="Feuchtezahl",
                    ),
                ),
                (
                    "humid_extra",
                    models.CharField(
                        blank=True,
                        choices=[("~", "~"), ("(?)", "(?)")],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "react_number",
                    models.CharField(
                        blank=True,
                        choices=[
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
                            (
                                "R9 - Basen- und Kalkzeiger",
                                "R9 - Basen- und Kalkzeiger",
                            ),
                            (
                                "Rx - indifferentes Verhalten",
                                "Rx - indifferentes Verhalten",
                            ),
                            (
                                "R? - ungeklärtes Verhalten",
                                "R? - ungeklärtes Verhalten",
                            ),
                            ("nicht angegeben", "nicht angegeben"),
                        ],
                        max_length=100,
                        null=True,
                        verbose_name="Reaktionszahl",
                    ),
                ),
                (
                    "react_extra",
                    models.CharField(
                        blank=True,
                        choices=[("~", "~"), ("(?)", "(?)")],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "nutri_number",
                    models.CharField(
                        blank=True,
                        choices=[
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
                            (
                                "N5 - mäßig stickstoffreiche Standorte",
                                "N5 - mäßig stickstoffreiche Standorte",
                            ),
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
                            (
                                "Nx - indifferentes Verhalten",
                                "Nx - indifferentes Verhalten",
                            ),
                            (
                                "N? - ungeklärtes Verhalten",
                                "N? - ungeklärtes Verhalten",
                            ),
                            ("nicht angegeben", "nicht angegeben"),
                        ],
                        max_length=100,
                        null=True,
                        verbose_name="Stickstoff/Nährstoffzahl",
                    ),
                ),
                (
                    "nutri_extra",
                    models.CharField(
                        blank=True,
                        choices=[("~", "~"), ("(?)", "(?)")],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "plant",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="zeigernumber",
                        to="dive_content.Plant",
                        verbose_name="Pflanze",
                    ),
                ),
            ],
            options={
                "verbose_name": "Zeigerzahl",
                "verbose_name_plural": "Zeigerzahlen",
            },
        ),
    ]