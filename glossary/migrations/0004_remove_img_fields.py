# Generated by Django 3.0.6 on 2020-05-26 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("glossary", "0003_add_verbose_name_to_text_field"),
    ]

    operations = [
        migrations.RemoveField(model_name="glossaryentry", name="img",),
        migrations.RemoveField(model_name="glossaryentry", name="img_alt",),
    ]
