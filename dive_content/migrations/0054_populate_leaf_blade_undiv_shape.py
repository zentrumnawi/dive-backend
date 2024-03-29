# Generated by Django 3.0.8 on 2021-03-23 13:50

from django.db import migrations


def populate_leaf_blade_undiv_shape_with_leaf_form(apps, schema_editor):
    """
    Populate Leaf model blade_undiv_shape fields with form values.
    """
    Leaf = apps.get_model("dive_content", "Leaf")

    for obj in Leaf.objects.all():
        if obj.form:
            obj.blade_undiv_shape = [obj.form]
        else:
            obj.blade_undiv_shape = []
        obj.save()


def populate_leaf_form_with_leaf_blade_undiv_shape(apps, schema_editor):
    """
    Populate Leaf model form fields with blade_undiv_shape first values.
    """
    Leaf = apps.get_model("dive_content", "Leaf")

    for obj in Leaf.objects.all():
        if obj.blade_undiv_shape:
            obj.form = obj.blade_undiv_shape[0]
        else:
            obj.form = ""
        obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0053_populate_leaf_blade_subdiv_shape"),
    ]

    operations = [
        migrations.RunPython(
            populate_leaf_blade_undiv_shape_with_leaf_form,
            populate_leaf_form_with_leaf_blade_undiv_shape,
        ),
    ]
