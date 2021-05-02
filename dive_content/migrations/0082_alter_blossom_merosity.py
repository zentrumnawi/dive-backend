# Generated by Django 3.0.8 on 2021-05-01 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0081_bulk_remove_blossom"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blossom",
            name="merosity",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (None, "-"),
                    (1, 1),
                    (2, 2),
                    (3, 3),
                    (4, 4),
                    (5, 5),
                    (6, 6),
                    (7, 7),
                    (8, 8),
                    (9, "viel"),
                ],
                null=True,
                verbose_name="Zähligkeit",
            ),
        ),
    ]
