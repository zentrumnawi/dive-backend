# Generated by Django 3.0.8 on 2021-03-23 13:50

from django.db import migrations


def populate_leaf_incision_depth_with_leaf_dep_cuts(apps, schema_editor):
    """
    Populate Leaf model incision_depth fields with dep_cuts values.
    """
    Leaf = apps.get_model("dive_content", "Leaf")

    for obj in Leaf.objects.all():
        if obj.dep_cuts:
            obj.incision_depth = [obj.dep_cuts]
        else:
            obj.incision_depth = []
        obj.save()


def populate_leaf_dep_cuts_with_leaf_incision_depth(apps, schema_editor):
    """
    Populate Leaf model dep_cuts fields with incision_depth first values.
    """
    Leaf = apps.get_model("dive_content", "Leaf")

    for obj in Leaf.objects.all():
        if obj.incision_depth:
            obj.dep_cuts = obj.incision_depth[0]
        else:
            obj.dep_cuts = ""
        obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0051_populate_leaf_attachment"),
    ]

    operations = [
        migrations.RunPython(
            populate_leaf_incision_depth_with_leaf_dep_cuts,
            populate_leaf_dep_cuts_with_leaf_incision_depth,
        ),
    ]
