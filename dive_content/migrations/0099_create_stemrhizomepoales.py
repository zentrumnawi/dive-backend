# Generated by Django 3.0.8 on 2021-09-13 06:58
import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0098_create_blossompoales"),
    ]

    operations = [
        migrations.CreateModel(
            name="StemRhizomePoales",
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
                    "tuft_stolon",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("loH", "lockerer Horst"),
                            ("auH", "ausgebreiteter Horst"),
                            ("dfH", "dichter, fester Horst"),
                            ("obA", "oberirdische Ausläufer (Stolone)"),
                            ("unA", "unterirdische Ausläufer (Rhizome)"),
                        ],
                        max_length=3,
                        verbose_name="Horst/Ausläufer",
                    ),
                ),
                (
                    "stem_color",
                    models.CharField(
                        blank=True,
                        help_text="Grammatikalisch anpassen.",
                        max_length=50,
                        verbose_name="Farbe",
                    ),
                ),
                (
                    "stem_hairiness",
                    models.CharField(
                        blank=True,
                        choices=[("g", "glatt"), ("k", "kahl"), ("b", "behaart")],
                        max_length=1,
                        verbose_name="Behaarung",
                    ),
                ),
                (
                    "stem_cross_section",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(
                            choices=[
                                ("sti", "stilrund"),
                                ("fla", "flachgedrückt"),
                                ("std", "stumpf dreikantig"),
                                ("scd", "scharf dreikantig"),
                                ("dre", "dreikantig"),
                            ],
                            max_length=3,
                        ),
                        blank=True,
                        default=list,
                        size=2,
                        verbose_name="Querschnitt",
                    ),
                ),
                (
                    "stem_pith",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("h", "hohl"),
                            ("n", "hohl; nur Knoten markig"),
                            ("m", "markig"),
                        ],
                        max_length=1,
                        verbose_name="Mark",
                    ),
                ),
                (
                    "stem_nodes",
                    models.CharField(
                        blank=True,
                        choices=[("m", "mit Knoten"), ("o", "ohne Knoten")],
                        max_length=1,
                        verbose_name="Knoten",
                    ),
                ),
                (
                    "stem_nodes_hairiness",
                    models.CharField(
                        blank=True,
                        choices=[("k", "kahl"), ("b", "behaart")],
                        max_length=1,
                        verbose_name="Behaarung (Knoten)",
                    ),
                ),
                (
                    "stem_transverse_walls",
                    models.CharField(
                        blank=True,
                        choices=[("m", "mit Querwänden"), ("o", "ohne Querwände")],
                        max_length=1,
                        verbose_name="Querwände",
                    ),
                ),
                (
                    "stem_surface",
                    models.CharField(
                        blank=True, max_length=10, verbose_name="Oberfläche"
                    ),
                ),
                (
                    "stem_features",
                    models.CharField(
                        blank=True,
                        help_text="Als eigenständigen Satz ausformulieren.",
                        max_length=100,
                        verbose_name="Besonderheiten",
                    ),
                ),
                (
                    "rhizome_length",
                    models.CharField(
                        blank=True,
                        choices=[("k", "kurz"), ("m", "mittellang"), ("l", "lang")],
                        max_length=1,
                        verbose_name="Länge",
                    ),
                ),
                (
                    "rhizome_branching",
                    models.CharField(
                        blank=True,
                        choices=[("g", "gering verzweigt"), ("s", "stark verzweigt")],
                        max_length=1,
                        verbose_name="Verzweigung",
                    ),
                ),
                (
                    "plant",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stemrhizomepoales",
                        to="dive_content.Plant",
                        verbose_name="Pflanze",
                    ),
                ),
            ],
            options={
                "verbose_name": "Halm und Rhizom (Poales)",
                "verbose_name_plural": "Halme und Rhizome (Poales)",
            },
        ),
    ]
