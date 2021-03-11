# Generated by Django 3.0.8 on 2021-03-11 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0075_rename_leaf_thick_flesch"),
    ]

    operations = [
        migrations.AlterField(
            model_name="leaf",
            name="succulence",
            field=models.CharField(
                blank=True,
                choices=[("dic", "dickfleischig"), ("ndi", "nicht dickfleischig")],
                default="",
                max_length=3,
                verbose_name="Dickfleischigkeit",
            ),
            preserve_default=False,
        ),
    ]
