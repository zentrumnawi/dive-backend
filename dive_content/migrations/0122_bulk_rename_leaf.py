# Generated by Django 3.0.8 on 2022-01-24 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0121_bulk_remove_stemroot"),
    ]

    operations = [
        migrations.RenameField(
            model_name="leaf", old_name="rosette", new_name="basal_leaf_rosette",
        ),
        migrations.RenameField(
            model_name="leaf",
            old_name="leaf_comp_incision_depth",
            new_name="compound_leaf_incision_depth",
        ),
        migrations.RenameField(
            model_name="leaf",
            old_name="leaf_comp_incision_num",
            new_name="compound_leaf_incision_number",
        ),
        migrations.RenameField(
            model_name="leaf",
            old_name="leaf_comp_num",
            new_name="compound_leaf_number",
        ),
        migrations.RenameField(
            model_name="leaf",
            old_name="leaf_comp_blade_shape",
            new_name="compound_leaf_shape",
        ),
        migrations.RenameField(
            model_name="leaf",
            old_name="leaflet_incision_add",
            new_name="leaflet_incision_addition",
        ),
        migrations.RenameField(
            model_name="leaf",
            old_name="leaflet_incision_num",
            new_name="leaflet_incision_number",
        ),
        migrations.RenameField(
            model_name="leaf", old_name="seed_leaf_num", new_name="seed_leaf_number",
        ),
        migrations.RenameField(
            model_name="leaf",
            old_name="leaf_simple_incision_depth",
            new_name="simple_leaf_incision_depth",
        ),
        migrations.RenameField(
            model_name="leaf",
            old_name="leaf_simple_incision_num",
            new_name="simple_leaf_incision_number",
        ),
        migrations.RenameField(
            model_name="leaf",
            old_name="leaf_simple_num",
            new_name="simple_leaf_number",
        ),
        migrations.RenameField(
            model_name="leaf",
            old_name="leaf_simple_blade_shape",
            new_name="simple_leaf_shape",
        ),
        migrations.RenameField(
            model_name="leaf", old_name="veins", new_name="venation",
        ),
    ]
