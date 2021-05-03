# Generated by Django 3.0.8 on 2021-03-24 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0063_rename_sprout_to_stemroot"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="stemroot",
            options={
                "verbose_name": "Spross und Wurzel",
                "verbose_name_plural": "Sprosse und Wurzeln",
            },
        ),
        migrations.AlterField(
            model_name="stemroot",
            name="plant",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="stemroot",
                to="dive_content.Plant",
                verbose_name="Pflanze",
            ),
        ),
    ]
