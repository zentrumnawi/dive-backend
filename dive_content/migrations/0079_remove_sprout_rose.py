# Generated by Django 3.0.8 on 2021-03-11 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0078_populate_leaf_rosette"),
    ]

    operations = [
        migrations.RemoveField(model_name="sprout", name="rose",),
    ]
