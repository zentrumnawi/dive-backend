# Generated by Django 3.0.8 on 2020-07-26 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0016_provide_verbose_names"),
    ]

    operations = [
        migrations.AddField(
            model_name="leaf",
            name="thick_flesh",
            field=models.CharField(
                blank=True,
                choices=[("yes", "ja"), ("no", "nein")],
                max_length=3,
                null=True,
                verbose_name="Dickfleischig",
            ),
        ),
        migrations.AlterField(
            model_name="blossom",
            name="griffel_sub",
            field=models.CharField(
                choices=[
                    ("end", "subendständig"),
                    ("sei", "subseitenständig"),
                    ("gru", "subgrundständig"),
                    ("gyn", "subgynobasisch"),
                ],
                max_length=3,
                verbose_name="Ständigkeit des Griffels ist sub-",
            ),
        ),
        migrations.AlterField(
            model_name="plant",
            name="nodule",
            field=models.CharField(
                blank=True,
                choices=[("yes", "ja"), ("no", "nein")],
                max_length=3,
                null=True,
                verbose_name="Wurzelknollen",
            ),
        ),
        migrations.AlterField(
            model_name="sprout",
            name="milk",
            field=models.CharField(
                blank=True, max_length=3, null=True, verbose_name="Milchsaft"
            ),
        ),
        migrations.AlterField(
            model_name="sprout",
            name="rose",
            field=models.CharField(
                blank=True, max_length=3, null=True, verbose_name="Grundblattrose"
            ),
        ),
        migrations.AlterField(
            model_name="sprout",
            name="thick_flesh",
            field=models.CharField(
                blank=True,
                choices=[("yes", "ja"), ("no", "nein")],
                max_length=3,
                null=True,
                verbose_name="Dickfleischig",
            ),
        ),
    ]
