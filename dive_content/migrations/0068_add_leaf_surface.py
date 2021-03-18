# Generated by Django 3.0.8 on 2021-03-10 08:22

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0067_remove_leaf_leaflets"),
    ]

    operations = [
        migrations.AddField(
            model_name="leaf",
            name="surface",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    choices=[
                        ("gla", "glatt"),
                        ("run", "runzelig"),
                        ("rau", "rauh"),
                        ("vra", "vorwärts rauh"),
                        ("ber", "bereift"),
                        ("bes", "bestäubt/bemehlt"),
                        ("pap", "papillös"),
                        ("pun", "punktiert"),
                        ("swi", "schwielig"),
                        ("kah", "kahl"),
                        ("ver", "verkahlend"),
                        ("fla", "flaumhaarig/weichhaarig"),
                        ("sei", "seidenhaarig"),
                        ("spi", "spinnwebig"),
                        ("flo", "flockig"),
                        ("sam", "samthaarig"),
                        ("fil", "filzig"),
                        ("wol", "wollig"),
                        ("zot", "zottig"),
                        ("rah", "rauhaarig"),
                        ("ste", "steifhaarig"),
                        ("gew", "gewimpert"),
                        ("dru", "drüsenhaarig"),
                        ("ste", "sternhaarig"),
                        ("sdh", "schildhaarig"),
                        ("sup", "schuppenhaarig/schuppig"),
                        ("sue", "schülferig"),
                        ("bae", "bärtig"),
                        ("ach", "achselbärtig"),
                        ("nac", "nackt"),
                    ],
                    max_length=3,
                    verbose_name="Blattoberfläche",
                ),
                blank=True,
                default=list,
                size=2,
            ),
        ),
    ]