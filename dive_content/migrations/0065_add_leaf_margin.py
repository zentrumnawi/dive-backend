# Generated by Django 3.0.8 on 2021-03-10 07:30

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0064_remove_leaf_form"),
    ]

    operations = [
        migrations.AddField(
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
                        ("ges", "geschweift"),
                        ("bew", "bewimpert"),
                        ("vor", "vorwärts rauh"),
                        ("rra", "rückwärts rauh"),
                    ],
                    max_length=3,
                    verbose_name="Spreiten-/Blättchenrand",
                ),
                blank=True,
                default=list,
                size=2,
            ),
        ),
    ]
