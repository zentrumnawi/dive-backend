# Generated by Django 3.0.8 on 2021-03-24 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0070_bulk_remove_stemroot"),
    ]

    operations = [
        migrations.RenameField(
            model_name="stemroot", old_name="leafly", new_name="bracts",
        ),
        migrations.RenameField(
            model_name="stemroot", old_name="milk", new_name="milky_sap",
        ),
        migrations.RenameField(
            model_name="stemroot", old_name="thick_flesh", new_name="succulence",
        ),
    ]
