# Generated by Django 3.0.5 on 2020-04-10 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0011_change_plant_habitat_choices'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaf',
            name='spr_structure',
            field=models.CharField(blank=True, choices=[('ei', 'Einschnitte'), ('bl', 'Blättchen')], max_length=2, verbose_name='Struktur der Blattspreite'),
        ),
    ]
