# Generated by Django 3.0.8 on 2021-12-13 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0105_update_plant_growth_form"),
    ]

    operations = [
        migrations.RemoveField(model_name="plant", name="alt_trivial_name",),
        migrations.RemoveField(model_name="plant", name="ground_to_be_removed",),
        migrations.RemoveField(model_name="plant", name="habitat",),
    ]
