# Generated by Django 3.0.8 on 2021-03-01 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0027_remove_plant_systematics"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plant",
            name="bloom",
            field=models.CharField(
                blank=True, max_length=200, verbose_name="Blütezeit"
            ),
        ),
    ]
