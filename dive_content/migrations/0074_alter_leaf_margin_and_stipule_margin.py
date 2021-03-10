# Generated by Django 3.0.8 on 2021-03-10 09:52

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0073_remove_leaf_side_leaf"),
    ]

    operations = [
        migrations.AlterField(
            model_name="leaf",
            name="margin",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    choices=[
                        ("dor", "dornig"),
                        ("gan", "ganzrandig"),
                        ("ges", "gesägt"),
                        ("dop", "doppelt gesägt"),
                        ("rue", "rückwärts gesägt"),
                        ("gez", "gezähnt"),
                        ("gzt", "gezähnelt"),
                        ("gef", "gefranst"),
                        ("gek", "gekerbt"),
                        ("geb", "gebuchtet"),
                        ("gew", "geschweift"),
                        ("bew", "bewimpert"),
                        ("vor", "vorwärts rauh"),
                        ("rur", "rückwärts rauh"),
                    ],
                    max_length=3,
                    verbose_name="Spreiten-/Blättchenrand",
                ),
                blank=True,
                default=list,
                size=2,
            ),
        ),
        migrations.AlterField(
            model_name="leaf",
            name="stipule_margin",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    choices=[
                        ("dor", "dornig"),
                        ("gan", "ganzrandig"),
                        ("ges", "gesägt"),
                        ("dop", "doppelt gesägt"),
                        ("rue", "rückwärts gesägt"),
                        ("gez", "gezähnt"),
                        ("gzt", "gezähnelt"),
                        ("gef", "gefranst"),
                        ("gek", "gekerbt"),
                        ("geb", "gebuchtet"),
                        ("gew", "geschweift"),
                        ("bew", "bewimpert"),
                        ("vor", "vorwärts rauh"),
                        ("rur", "rückwärts rauh"),
                    ],
                    max_length=3,
                    verbose_name="Nebenblattrand",
                ),
                blank=True,
                default=list,
                size=2,
            ),
        ),
    ]
