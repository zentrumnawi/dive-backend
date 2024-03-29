# Generated by Django 3.0.8 on 2022-01-14 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0114_bulk_rename_fruit"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fruit",
            name="fruit_color_shape",
            field=models.CharField(
                blank=True,
                help_text="Grammatikalisch anpassen.",
                max_length=100,
                verbose_name="Farbe/Gestalt",
            ),
        ),
        migrations.AlterField(
            model_name="fruit",
            name="fruit_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("ach", "Achäne"),
                    ("apf", "Apfelfrucht"),
                    ("bal", "Balgfrucht"),
                    ("bac", "Balgfrüchtchen"),
                    ("bee", "Beere"),
                    ("bru", "Bruchfrucht"),
                    ("dop", "Doppelachäne"),
                    ("glh", "Gliederhülse"),
                    ("gls", "Gliederschote"),
                    ("hue", "Hülse"),
                    ("kap", "Kapsel"),
                    ("kar", "Karyopse"),
                    ("kla", "Klausenfrucht"),
                    ("kok", "Kokke"),
                    ("nus", "Nuss"),
                    ("nue", "Nüsschen"),
                    ("sam", "Sammelbalgfrucht"),
                    ("soe", "Schötchen"),
                    ("smf", "Schote mit falscher Scheidewand"),
                    ("sos", "Schote ohne Scheidewand"),
                    ("spa", "Spaltfrucht"),
                    ("ste", "Steinfrucht"),
                    ("stc", "Steinfrüchtchen"),
                ],
                max_length=3,
                verbose_name="Typ",
            ),
        ),
        migrations.AlterField(
            model_name="fruit",
            name="ovule_position",
            field=models.CharField(
                blank=True,
                choices=[
                    ("fr", "Fruchtknoten (Angiospermen)"),
                    ("za", "Zapfenschuppe (Gymnospermen)"),
                ],
                max_length=2,
                verbose_name="Lage",
            ),
        ),
        migrations.AlterField(
            model_name="fruit",
            name="seed_color_shape",
            field=models.CharField(
                blank=True,
                help_text="Grammatikalisch anpassen.",
                max_length=100,
                verbose_name="Farbe/Gestalt",
            ),
        ),
        migrations.AlterField(
            model_name="fruit",
            name="seed_number",
            field=models.CharField(blank=True, max_length=10, verbose_name="Anzahl"),
        ),
        migrations.AlterField(
            model_name="fruit",
            name="winging",
            field=models.CharField(
                blank=True, max_length=100, verbose_name="Beflügelung"
            ),
        ),
    ]
