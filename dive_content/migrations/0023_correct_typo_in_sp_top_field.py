# Generated by Django 3.0.8 on 2021-01-05 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0022_add_blank_to_facts_to_know_field"),
    ]

    operations = [
        migrations.AlterField(
            model_name="leaf",
            name="sp_top",
            field=models.CharField(
                blank=True,
                choices=[
                    ("abg", "abgerundet"),
                    ("ges", "gestutzt"),
                    ("stu", "stumpf"),
                    ("spi", "spitz"),
                    ("zug", "zugespitzt"),
                    ("beg", "begrannt"),
                    ("sta", "stachelspitze"),
                    ("haa", "haarspitzig"),
                    ("bes", "bespitzt"),
                    ("aus", "ausgerandet"),
                ],
                max_length=3,
                verbose_name="Spreitenspitze",
            ),
        ),
    ]