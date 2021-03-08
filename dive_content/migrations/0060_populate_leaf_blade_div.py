# Generated by Django 3.0.8 on 2021-03-08 09:26

from django.db import migrations


def populate_leaf_blade_div_with_leaf_arr_cuts(apps, schema_editor):
    """
    Populate leaf model blade_div fields with arr_cuts values.
    """
    Leaf = apps.get_model("dive_content", "Leaf")

    for obj in Leaf.objects.all():
        if obj.arr_cuts:
            obj.blade_div = [obj.arr_cuts]
        else:
            obj.blade_div = []
        obj.save()


def populate_leaf_arr_cuts_with_leaf_blade_div(apps, schema_editor):
    """
    Populate leaf model arr_cuts fields with blade_div first values.
    """
    Leaf = apps.get_model("dive_content", "Leaf")

    for obj in Leaf.objects.all():
        if obj.blade_div:
            obj.arr_cuts = obj.blade_div[0]
        else:
            obj.arr_cuts = ""
        obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0059_add_leaf_blade_div"),
    ]

    operations = [
        migrations.RunPython(
            populate_leaf_blade_div_with_leaf_arr_cuts,
            populate_leaf_arr_cuts_with_leaf_blade_div,
        ),
    ]