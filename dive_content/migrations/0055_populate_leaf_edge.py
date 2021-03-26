# Generated by Django 3.0.8 on 2021-03-23 13:50

from django.db import migrations


def populate_leaf_edge_with_leaf_leaflets(apps, schema_editor):
    """
    Populate leaf model edge fields with leaflets values.
    """
    Leaf = apps.get_model("dive_content", "Leaf")

    for obj in Leaf.objects.all():
        if obj.leaflets:
            obj.edge = [obj.leaflets]
        else:
            obj.edge = []
        obj.save()


def populate_leaf_leaflets_with_leaf_edge(apps, schema_editor):
    """
    Populate leaf model leaflets fields with edge first values.
    """
    Leaf = apps.get_model("dive_content", "Leaf")

    for obj in Leaf.objects.all():
        if obj.edge:
            obj.leaflets = obj.edge[0]
        else:
            obj.leaflets = ""
        obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0054_populate_leaf_blade_undiv_shape"),
    ]

    operations = [
        migrations.RunPython(
            populate_leaf_edge_with_leaf_leaflets,
            populate_leaf_leaflets_with_leaf_edge,
        ),
    ]