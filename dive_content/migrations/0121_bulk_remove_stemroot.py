# Generated by Django 3.0.8 on 2022-01-18 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0120_bulk_populate_stemroot"),
    ]

    operations = [
        migrations.RemoveField(model_name="stemroot", name="bracts",),
        migrations.RemoveField(
            model_name="stemroot", name="creep_lay_shoots_to_be_replaced",
        ),
        migrations.RemoveField(model_name="stemroot", name="runners_to_be_replaced",),
    ]