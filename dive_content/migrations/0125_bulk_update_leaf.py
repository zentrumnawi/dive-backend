# Generated by Django 3.0.8 on 2022-01-24 15:50

from django.db import migrations


def prune_leaf_basal_leaf_rosette(apps, schema_editor):
    Leaf = apps.get_model("dive_content", "Leaf")

    objects = list(Leaf.objects.exclude(basal_leaf_rosette=""))
    for obj in objects:
        obj.basal_leaf_rosette = ""
    Leaf.objects.bulk_update(objects, ["basal_leaf_rosette"])


def bulk_update_leaf_fields(apps, schema_editor):
    Leaf = apps.get_model("dive_content", "Leaf")

    objects = Leaf.objects.exclude(
        compound_leaf_incision_number="",
        leaflet_incision_number="",
        simple_leaf_incision_number="",
    )
    for obj in objects:
        obj.compound_leaf_incision_number = obj.compound_leaf_incision_number.split(
            "-", 1
        )[0]
        obj.leaflet_incision_number = obj.leaflet_incision_number.split("-", 1)[0]
        obj.simple_leaf_incision_number = obj.simple_leaf_incision_number.split("-", 1)[
            0
        ]
    Leaf.objects.bulk_update(
        objects,
        [
            "compound_leaf_incision_number",
            "leaflet_incision_number",
            "simple_leaf_incision_number",
        ],
    )


def prune_leaf_seed_leaf_number(apps, schema_editor):
    Leaf = apps.get_model("dive_content", "Leaf")

    objects = list(Leaf.objects.filter(seed_leaf_number=3))
    for obj in objects:
        obj.seed_leaf_number = None
    Leaf.objects.bulk_update(objects, ["seed_leaf_number"])


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0124_bulk_alter_leaf"),
    ]

    operations = [
        migrations.RunPython(migrations.RunPython.noop, prune_leaf_basal_leaf_rosette),
        migrations.RunPython(migrations.RunPython.noop, bulk_update_leaf_fields),
        migrations.RunPython(migrations.RunPython.noop, prune_leaf_seed_leaf_number),
    ]
