# Generated by Django 3.0.5 on 2020-04-08 14:55

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0009_blank_instead_of_default_empty_string"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plant",
            name="habitat",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    choices=[
                        ("sch", "Schlammfluren"),
                        ("roe", "Röhrichte"),
                        ("sae", "Säume"),
                        ("sta", "Staudenfluren"),
                        ("gru", "Grünland und Zwergstrauchheiden"),
                        ("rud", "Ruderalvegetation"),
                        ("aec", "Äcker"),
                        ("wei", "Weinberge"),
                        ("int", "Intensivgrünland"),
                        ("par", "Parks"),
                        ("gae", "Gärten"),
                        ("tri", "Trittpflanzengesellschaften"),
                        ("fel", "Felsbiotope"),
                        ("aue", "Auenwälder"),
                        ("geb", "Gebüsche"),
                        ("ext", "Extensivgrünland oder natürlicher Rasen"),
                        ("wae", "Wälder"),
                        ("ufe", "Ufer"),
                    ],
                    max_length=3,
                ),
                blank=True,
                size=None,
                verbose_name="Lebensraum",
            ),
        ),
    ]
