# Generated by Django 3.0.8 on 2021-04-15 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0075_delete_zeigernumber"),
    ]

    operations = [
        migrations.RenameField(
            model_name="blossom", old_name="season", new_name="season_old",
        ),
    ]
