# Generated by Django 3.0.8 on 2021-03-07 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0057_rename_leaf_dep_cuts_array"),
    ]

    operations = [
        migrations.RemoveField(model_name="leaf", name="arr_special",),
    ]
