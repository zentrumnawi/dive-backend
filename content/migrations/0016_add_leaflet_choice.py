# Generated by Django 3.0.5 on 2020-04-14 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0015_add_habitat_choice"),
    ]

    operations = [
        migrations.AlterField(
            model_name="leaf",
            name="leaflets",
            field=models.CharField(
                blank=True,
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
                verbose_name="Spreiten/Blättchen",
            ),
        ),
    ]
