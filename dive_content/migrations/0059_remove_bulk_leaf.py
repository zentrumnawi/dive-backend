# Generated by Django 3.0.8 on 2021-03-23 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0058_populate_leaf_rosette"),
    ]

    operations = [
        migrations.RemoveField(model_name="leaf", name="spr_structure",),
        migrations.RemoveField(model_name="leaf", name="count",),
        migrations.RemoveField(model_name="leaf", name="arr_special",),
        migrations.RemoveField(model_name="leaf", name="att_axis",),
        migrations.RemoveField(model_name="leaf", name="dep_cuts",),
        migrations.RemoveField(model_name="leaf", name="arr_cuts",),
        migrations.RemoveField(model_name="leaf", name="form",),
        migrations.RemoveField(model_name="leaf", name="leaflets",),
        migrations.RemoveField(model_name="leaf", name="sur_texture",),
        migrations.RemoveField(model_name="leaf", name="side_leaf",),
        migrations.RemoveField(model_name="sprout", name="rose",),
    ]
