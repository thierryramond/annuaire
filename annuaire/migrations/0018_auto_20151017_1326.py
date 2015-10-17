# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annuaire', '0017_auto_20151015_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='membrenew',
            name='date_naissance',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='membrenew',
            name='position',
            field=models.CharField(null=True, max_length=50, blank=True, choices=[('activité', 'activité'), ('associé', 'associé'), ('CDD', 'CDD'), ('décès', 'décès'), ('détachement', 'détachement'), ('disponibilité', 'disponibilité'), ('émérite', 'émérite'), ('parti', 'parti'), ('retraité', 'retraité')]),
        ),
    ]
