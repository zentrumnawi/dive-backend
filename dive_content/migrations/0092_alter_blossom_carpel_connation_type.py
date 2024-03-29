# Generated by Django 3.0.8 on 2021-05-02 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0091_update_stemroot_cross_section"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blossom",
            name="carpel_connation_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("ap", "apokarp (chorikarp, unverwachsen)"),
                    ("mo", "monokarp"),
                    ("co", "coenocarp (verwachsen)"),
                    ("cs", "coeno-synkarp verwachsen"),
                    ("cp", "coeno-parakarp verwachsen"),
                ],
                max_length=2,
                verbose_name="Verwachsungstyp (Fruchtblatt)",
            ),
        ),
    ]
