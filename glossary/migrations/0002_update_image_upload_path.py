# Generated by Django 3.0.3 on 2020-04-24 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("glossary", "0001_implement_glossary_entry_model"),
    ]

    operations = [
        migrations.AlterField(
            model_name="glossaryentry",
            name="img",
            field=models.ImageField(blank=True, null=True, upload_to="glossary/"),
        ),
    ]
