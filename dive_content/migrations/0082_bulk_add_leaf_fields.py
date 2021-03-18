# Generated by Django 3.0.8 on 2021-03-18 04:47

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0081_bulk_alter_leaf_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="leaf",
            name="incision_num",
            field=models.CharField(
                blank=True, max_length=10, verbose_name="Einschnittanzahl"
            ),
        ),
        migrations.AddField(
            model_name="leaf",
            name="leaf_comp_num",
            field=models.CharField(
                blank=True, max_length=10, verbose_name="Blattanzahl (zusg. Blätter)"
            ),
        ),
        migrations.AddField(
            model_name="leaf",
            name="leaf_simple_num",
            field=models.CharField(
                blank=True, max_length=10, verbose_name="Blattanzahl (einf. Blätter)"
            ),
        ),
        migrations.AddField(
            model_name="leaf",
            name="leaflet_incision_add",
            field=models.CharField(
                blank=True, max_length=100, verbose_name="Einschnittzusatz (Blättchen)"
            ),
        ),
        migrations.AddField(
            model_name="leaf",
            name="leaflet_incision_depth",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    choices=[
                        ("gan", "ganz/ungeteilt"),
                        ("gel", "gelappt"),
                        ("gep", "gespalten"),
                        ("get", "geteilt"),
                        ("ges", "geschnitten"),
                        ("gef", "gefingert"),
                        ("zus", "zusammengesetzt"),
                        ("fis", "fiederschnittig"),
                        ("fie", "gefiedert"),
                    ],
                    max_length=3,
                    verbose_name="Einschnitttiefe (Blättchen)",
                ),
                blank=True,
                default=list,
                size=2,
            ),
        ),
        migrations.AddField(
            model_name="leaf",
            name="leaflet_incision_num",
            field=models.CharField(
                blank=True, max_length=10, verbose_name="Einschnittanzahl (Blättchen)"
            ),
        ),
    ]