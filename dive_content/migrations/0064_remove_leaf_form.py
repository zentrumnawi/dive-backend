# Generated by Django 3.0.8 on 2021-03-08 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0063_populate_leaf_blade_undiv"),
    ]

    operations = [
        migrations.RemoveField(model_name="leaf", name="form",),
    ]
