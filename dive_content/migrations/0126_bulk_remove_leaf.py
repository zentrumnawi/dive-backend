# Generated by Django 3.0.8 on 2022-01-26 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0125_bulk_update_leaf"),
    ]

    operations = [
        migrations.RemoveField(model_name="leaf", name="sheath",),
        migrations.RemoveField(model_name="leaf", name="stipule_edge",),
    ]