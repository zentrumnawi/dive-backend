# Generated by Django 3.0.8 on 2021-03-23 13:50

from django.db import migrations, models


def update_leaf_arr_cuts_forwards(apps, schema_editor):
    ARR_CUTS_UPDATE_FORWARDS = {
        "han": "",
        "hgl": "han",
        "hgt": "han",
        "hgs": "han",
        "fie": "fif",
        "unf": "unt",
        "ung": "unt",
        "dog": "dop",
        "fug": "fus",
        "fuz": "fus",
    }

    Leaf = apps.get_model("dive_content", "Leaf")

    for obj in Leaf.objects.all():
        if obj.arr_cuts in ARR_CUTS_UPDATE_FORWARDS.keys():
            obj.arr_cuts = ARR_CUTS_UPDATE_FORWARDS.get(obj.arr_cuts)
            obj.save()


def update_leaf_arr_cuts_reverse(apps, schema_editor):
    ARR_CUTS_UPDATE_REVERSE = {
        "han": "",
        "fif": "fie",
        "unt": "",
        "dop": "dog",
        "fus": "",
    }

    Leaf = apps.get_model("dive_content", "Leaf")

    for obj in Leaf.objects.all():
        if obj.arr_cuts in ARR_CUTS_UPDATE_REVERSE.keys():
            obj.arr_cuts = ARR_CUTS_UPDATE_REVERSE.get(obj.arr_cuts)
            obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0049_bulk_rename_leaf"),
    ]

    operations = [
        migrations.AlterField(
            model_name="leaf",
            name="division",
            field=models.CharField(
                blank=True,
                choices=[("ein", "einfach"), ("zus", "zusammengesetzt")],
                max_length=3,
                verbose_name="Spreitengliederung",
            ),
        ),
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
        migrations.AlterField(
            model_name="leaf",
            name="arrangement",
            field=models.CharField(
                blank=True,
                choices=[
                    ("gru", "grundständig"),
                    ("wec", "wechselständig/spiralig"),
                    ("zwe", "zweizeilig/distich"),
                    ("dre", "dreizeilig/tristich"),
                    ("geg", "gegenständig"),
                    ("kre", "kreuzgegenständig/dekussiert"),
                    ("gep", "gepaart"),
                    ("qui", "quirlig/wirtelig"),
                    ("sch", "scheinquirlig"),
                    ("dac", "dachziegelig"),
                    ("ein", "einseitig"),
                    ("ges", "gescheitelt"),
                ],
                max_length=3,
                verbose_name="Anordnung (an Sprossachse)",
            ),
        ),
        migrations.AlterField(
            model_name="leaf",
            name="apex",
            field=models.CharField(
                blank=True,
                choices=[
                    ("abg", "abgerundet"),
                    ("ges", "gestutzt"),
                    ("stu", "stumpf"),
                    ("spi", "spitz"),
                    ("zug", "zugespitzt"),
                    ("beg", "begrannt"),
                    ("sta", "stachelspitz"),
                    ("haa", "haarspitzig"),
                    ("bes", "bespitzt"),
                    ("aus", "ausgerandet"),
                ],
                max_length=3,
                verbose_name="Spreitenspitze",
            ),
        ),
        migrations.AlterField(
            model_name="leaf",
            name="special_features",
            field=models.CharField(
                blank=True,
                help_text='"Nicht vorhanden" eingeben, um hervorzuheben, dass kein ausgeprägtes Merkmal existiert.',
                max_length=200,
                verbose_name="Besondere Merkmale",
            ),
        ),
        migrations.AlterField(
            model_name="leaf",
            name="sheath",
            field=models.CharField(
                blank=True,
                help_text='"Nicht vorhanden" eingeben, um hervorzuheben, dass kein ausgeprägtes Merkmal existiert.',
                max_length=100,
                verbose_name="Blattscheide",
            ),
        ),
        migrations.AlterField(
            model_name="leaf",
            name="seed_leaf_num",
            field=models.IntegerField(
                blank=True,
                choices=[(1, 1), (2, 2)],
                null=True,
                verbose_name="Keimblattanzahl",
            ),
        ),
        migrations.AlterField(
            model_name="leaf",
            name="dep_cuts",
            field=models.CharField(
                blank=True,
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
                verbose_name="Tiefe von Einschnitten",
            ),
        ),
        migrations.RunPython(
            update_leaf_arr_cuts_forwards, update_leaf_arr_cuts_reverse
        ),
        migrations.AlterField(
            model_name="leaf",
            name="arr_cuts",
            field=models.CharField(
                blank=True,
                choices=[
                    ("han", "handförmig"),
                    ("gef", "gefingert"),
                    ("fif", "fiederförmig"),
                    ("fil", "fiederlappig"),
                    ("fip", "fiederspaltig"),
                    ("fit", "fiederteilig"),
                    ("fis", "fiederschnittig"),
                    ("paa", "paarig"),
                    ("unp", "unpaarig"),
                    ("unt", "unterbrochen"),
                    ("dop", "doppelt"),
                    ("meh", "mehrfach"),
                    ("dre", "dreizählig"),
                    ("dod", "doppelt dreizählig"),
                    ("lei", "leierförmig"),
                    ("sch", "schrotsägeförmig"),
                    ("kam", "kammförmig"),
                    ("fus", "fußförmig"),
                ],
                max_length=3,
                verbose_name="Anordnung der Spreite",
            ),
        ),
    ]
