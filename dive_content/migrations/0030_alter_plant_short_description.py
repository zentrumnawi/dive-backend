# Generated by Django 3.0.8 on 2021-03-02 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0029_rename_plant_facts_to_know"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plant",
            name="short_description",
            field=models.TextField(
                blank=True, default="", max_length=600, verbose_name="Kurzbeschreibung"
            ),
        ),
    ]
