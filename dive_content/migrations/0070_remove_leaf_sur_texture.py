# Generated by Django 3.0.8 on 2021-03-10 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0069_populate_leaf_surface"),
    ]

    operations = [
        migrations.RemoveField(model_name="leaf", name="sur_texture",),
    ]
