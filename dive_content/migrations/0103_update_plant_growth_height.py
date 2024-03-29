# Generated by Django 3.0.8 on 2021-09-07 10:28

from django.db import migrations


def prune_plant_growth_height(apps, schema_editor):
    Plant = apps.get_model("dive_content", "Plant")

    objects = list(Plant.objects.all())
    for obj in objects:
        obj.growth_height = ""
    Plant.objects.bulk_update(objects, ["growth_height"])


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0102_populate_plant_alternative_trivial_names"),
    ]

    operations = [
        migrations.RunPython(prune_plant_growth_height, migrations.RunPython.noop),
    ]
