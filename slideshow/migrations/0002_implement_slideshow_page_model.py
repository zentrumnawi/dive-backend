# Generated by Django 3.0.3 on 2020-04-09 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("slideshow", "0001_implement_slideshow_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="SlideshowPage",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("position", models.PositiveSmallIntegerField(default=1)),
                ("title", models.CharField(max_length=100)),
                ("text", models.TextField()),
                (
                    "show",
                    models.ForeignKey(
                        db_index=False,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="pages",
                        related_query_name="page",
                        to="slideshow.Slideshow",
                    ),
                ),
            ],
        ),
    ]
