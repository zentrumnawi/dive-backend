# Generated by Django 3.0.8 on 2021-03-03 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0030_alter_plant_short_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="blossom",
            name="season",
            field=models.CharField(
                blank=True,
                help_text="Bsp. (Januar) Februar bis März",
                max_length=200,
                verbose_name="Blütezeit",
            ),
        ),
    ]
