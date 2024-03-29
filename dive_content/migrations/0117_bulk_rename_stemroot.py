# Generated by Django 3.0.8 on 2022-01-18 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dive_content", "0116_remove_fruit_winging_feature"),
    ]

    operations = [
        migrations.RenameField(
            model_name="stemroot",
            old_name="creep_lay_shoots",
            new_name="creep_lay_shoots_to_be_replaced",
        ),
        migrations.RenameField(
            model_name="stemroot",
            old_name="organ_features",
            new_name="root_organ_features",
        ),
        migrations.RenameField(
            model_name="stemroot", old_name="organs", new_name="root_organs",
        ),
        migrations.RenameField(
            model_name="stemroot",
            old_name="primary_root",
            new_name="root_primary_root",
        ),
        migrations.RenameField(
            model_name="stemroot",
            old_name="runners",
            new_name="runners_to_be_replaced",
        ),
        migrations.RenameField(
            model_name="stemroot", old_name="appearance", new_name="stem_appearance",
        ),
        migrations.RenameField(
            model_name="stemroot",
            old_name="cross_section",
            new_name="stem_cross_section",
        ),
        migrations.RenameField(
            model_name="stemroot",
            old_name="orientation",
            new_name="stem_growth_orientation",
        ),
        migrations.RenameField(
            model_name="stemroot", old_name="pith", new_name="stem_pith",
        ),
        migrations.RenameField(
            model_name="stemroot", old_name="succulence", new_name="stem_succulence",
        ),
        migrations.RenameField(
            model_name="stemroot", old_name="surface", new_name="stem_surface",
        ),
    ]
