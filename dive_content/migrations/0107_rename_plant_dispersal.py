# Generated by Django 3.0.8 on 2021-12-14 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0106_bulk_remove_plant"),
    ]

    operations = [
        migrations.RenameField(
            model_name="plant", old_name="dispersal", new_name="dispersal_form",
        ),
    ]
