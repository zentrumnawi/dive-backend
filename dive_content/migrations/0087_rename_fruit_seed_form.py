# Generated by Django 3.0.8 on 2021-05-02 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0086_bulk_update_leaf_and_stemroot"),
    ]

    operations = [
        migrations.RenameField(
            model_name="fruit", old_name="seed_form", new_name="seed_color_form",
        ),
    ]
