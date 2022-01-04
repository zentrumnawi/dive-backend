# Generated by Django 3.0.8 on 2022-01-30 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0109_bulk_remove_blossom"),
    ]

    operations = [
        migrations.RenameField(
            model_name="blossom", old_name="bract_blade", new_name="bract_shape",
        ),
        migrations.RenameField(
            model_name="blossom", old_name="carpel_num", new_name="carpel_number",
        ),
        migrations.RenameField(
            model_name="blossom",
            old_name="blossom_num",
            new_name="inflorescence_blossom_number",
        ),
        migrations.RenameField(
            model_name="blossom",
            old_name="inflorescence_num",
            new_name="inflorescence_number",
        ),
        migrations.RenameField(
            model_name="blossom", old_name="ovary_pos", new_name="ovary_position",
        ),
        migrations.RenameField(
            model_name="blossom", old_name="perianth_form", new_name="perianth_shape",
        ),
        migrations.RenameField(
            model_name="blossom",
            old_name="petal_color_form",
            new_name="petal_color_shape",
        ),
        migrations.RenameField(
            model_name="blossom", old_name="petal_len", new_name="petal_length",
        ),
        migrations.RenameField(
            model_name="blossom", old_name="petal_num", new_name="petal_number",
        ),
        migrations.RenameField(
            model_name="blossom", old_name="pistil_pos", new_name="pistil_position",
        ),
        migrations.RenameField(
            model_name="blossom",
            old_name="sepal_color_form",
            new_name="sepal_color_shape",
        ),
        migrations.RenameField(
            model_name="blossom", old_name="sepal_num", new_name="sepal_number",
        ),
        migrations.RenameField(
            model_name="blossom",
            old_name="stamen_color_form",
            new_name="stamen_color_shape",
        ),
        migrations.RenameField(
            model_name="blossom",
            old_name="stamen_connation_type_add",
            new_name="stamen_connation_type_addition",
        ),
        migrations.RenameField(
            model_name="blossom", old_name="stamen_len", new_name="stamen_length",
        ),
        migrations.RenameField(
            model_name="blossom", old_name="stamen_num", new_name="stamen_number",
        ),
        migrations.RenameField(
            model_name="blossom", old_name="stigma_num", new_name="stigma_number",
        ),
    ]