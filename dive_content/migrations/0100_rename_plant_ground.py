# Generated by Django 3.0.8 on 2021-12-13 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0099_create_stemrhizomepoales"),
    ]

    operations = [
        migrations.RenameField(
            model_name="plant", old_name="ground", new_name="ground_to_be_removed",
        ),
    ]