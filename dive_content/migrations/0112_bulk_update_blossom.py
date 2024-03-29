# Generated by Django 3.0.8 on 2022-01-13 20:43

from django.db import migrations


def update_leaf_leaf_comp_blade_shape_forwards(apps, schema_editor):
    Leaf = apps.get_model("dive_content", "Leaf")

    for obj in Leaf.objects.filter(leaf_comp_blade_shape__contains=["dre"]):
        index = obj.leaf_comp_blade_shape.index("dre")
        obj.leaf_comp_blade_shape[index] = "drz"
        obj.save()


def update_leaf_leaf_comp_blade_shape_reverse(apps, schema_editor):
    Leaf = apps.get_model("dive_content", "Leaf")

    for obj in Leaf.objects.filter(leaf_comp_blade_shape__contains=["drz"]):
        index = obj.leaf_comp_blade_shape.index("drz")
        obj.leaf_comp_blade_shape[index] = "dre"
        obj.save()


def prune_blossom_inflorescence_type_reverse(apps, schema_editor):
    Blossom = apps.get_model("dive_content", "Blossom")

    for obj in Blossom.objects.filter(inflorescence_type="sca"):
        obj.inflorescence_type = ""
        obj.save()


def prune_blossom_bract_shape_forwards(apps, schema_editor):
    Blossom = apps.get_model("dive_content", "Blossom")

    for obj in Blossom.objects.filter(bract_shape__contains=["dre"]):
        obj.bract_shape.remove("dre")
        obj.save()


def prune_blossom_bract_shape_reverse(apps, schema_editor):
    Blossom = apps.get_model("dive_content", "Blossom")

    for obj in Blossom.objects.filter(bract_shape__overlap=["dre", "drz"]):
        if "dre" in obj.bract_shape:
            obj.bract_shape.remove("dre")
        if "drz" in obj.bract_shape:
            obj.bract_shape.remove("drz")
        obj.save()


def bulk_update_blossom_fields_forwards(apps, schema_editor):
    Blossom = apps.get_model("dive_content", "Blossom")

    objects = Blossom.objects.exclude(diameter="", petal_length="", stamen_length="")
    for obj in objects:
        obj.diameter = f"{obj.diameter} cm" if obj.diameter else ""
        obj.petal_length = f"{obj.petal_length} cm" if obj.petal_length else ""
        obj.stamen_length = f"{obj.stamen_length} cm" if obj.stamen_length else ""
    Blossom.objects.bulk_update(objects, ["diameter", "petal_length", "stamen_length"])


def bulk_update_blossom_fields_reverse(apps, schema_editor):
    Blossom = apps.get_model("dive_content", "Blossom")

    objects = Blossom.objects.exclude(diameter="", petal_length="", stamen_length="")
    for obj in objects:
        obj.diameter = obj.diameter.replace(" cm", "")[:10]
        obj.petal_length = obj.petal_length.replace(" cm", "")[:10]
        obj.stamen_length = obj.stamen_length.replace(" cm", "")[:10]
    Blossom.objects.bulk_update(objects, ["diameter", "petal_length", "stamen_length"])


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0111_bulk_alter_blossom"),
    ]

    operations = [
        migrations.RunPython(
            update_leaf_leaf_comp_blade_shape_forwards,
            update_leaf_leaf_comp_blade_shape_reverse,
        ),
        migrations.RunPython(
            migrations.RunPython.noop, prune_blossom_inflorescence_type_reverse
        ),
        migrations.RunPython(
            prune_blossom_bract_shape_forwards, prune_blossom_bract_shape_reverse
        ),
        migrations.RunPython(
            bulk_update_blossom_fields_forwards, bulk_update_blossom_fields_reverse
        ),
    ]
