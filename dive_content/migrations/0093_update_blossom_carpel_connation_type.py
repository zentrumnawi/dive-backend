# Generated by Django 3.0.8 on 2021-05-02 10:31

from django.db import migrations


def prune_blossom_carpel_connation_type(apps, schema_editor):
    Blossom = apps.get_model("dive_content", "Blossom")

    for obj in Blossom.objects.exclude(carpel_connation_type=""):
        if obj.carpel_connation_type == "co":
            obj.carpel_connation_type = ""
            obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0092_alter_blossom_carpel_connation_type"),
    ]

    operations = [
        migrations.RunPython(
            migrations.RunPython.noop, prune_blossom_carpel_connation_type
        ),
    ]
