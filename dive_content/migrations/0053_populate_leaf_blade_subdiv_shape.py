# Generated by Django 3.0.8 on 2021-03-23 13:50

from django.db import migrations


def populate_leaf_blade_subdiv_shape_with_leaf_arr_cuts(apps, schema_editor):
    """
    Populate leaf model blade_subdiv_shape fields with arr_cuts values.
    """
    Leaf = apps.get_model("dive_content", "Leaf")

    for obj in Leaf.objects.all():
        if obj.arr_cuts:
            obj.blade_subdiv_shape = [obj.arr_cuts]
        else:
            obj.blade_subdiv_shape = []
        obj.save()


def populate_leaf_arr_cuts_with_leaf_blade_subdiv_shape(apps, schema_editor):
    """
    Populate leaf model arr_cuts fields with blade_subdiv_shape first values.
    """
    Leaf = apps.get_model("dive_content", "Leaf")

    for obj in Leaf.objects.all():
        if obj.blade_subdiv_shape:
            obj.arr_cuts = obj.blade_subdiv_shape[0]
        else:
            obj.arr_cuts = ""
        obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0052_populate_leaf_incision_depth"),
    ]

    operations = [
        migrations.RunPython(
            populate_leaf_blade_subdiv_shape_with_leaf_arr_cuts,
            populate_leaf_arr_cuts_with_leaf_blade_subdiv_shape,
        ),
    ]
