# Generated by Django 3.0.8 on 2021-03-24 14:35

from django.db import migrations


def populate_stemroot_orientation_with_stemroot_pos(apps, schema_editor):
    """
    Populate StemRoot model orientation fields with pos values.
    """
    StemRoot = apps.get_model("dive_content", "StemRoot")

    for obj in StemRoot.objects.all():
        if obj.pos:
            if obj.pos in ("Ran", "Win", "Spr", "Wur"):
                obj.orientation = [obj.pos.lower()]
            else:
                obj.orientation = [obj.pos]
        else:
            obj.orientation = []
        obj.save()


def populate_stemroot_pos_with_stemroot_orientation(apps, schema_editor):
    """
    Populate StemRoot model pos fields with orientation first values.
    """
    StemRoot = apps.get_model("dive_content", "StemRoot")

    for obj in StemRoot.objects.all():
        if obj.orientation:
            if obj.orientation[0] in ("ran", "win", "spr", "wur"):
                obj.pos = obj.orientation[0].capitalize()
            else:
                obj.pos = obj.orientation[0]
        else:
            obj.pos = ""
        obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0065_bulk_add_stemroot"),
    ]

    operations = [
        migrations.RunPython(
            populate_stemroot_orientation_with_stemroot_pos,
            populate_stemroot_pos_with_stemroot_orientation,
        ),
    ]
