# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annuaire', '0016_auto_20151012_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membrenew',
            name='grade',
            field=models.CharField(null=True, blank=True, choices=[(None, 'sans objet'), ('POSTDOC', 'POSTDOC'), ('ATER', 'ATER'), ('CDD ATER', 'CDD ATER'), ('PRAG', 'PRAG'), ('MC', 'MC'), ('MC HC', 'MC HC'), ('CR2', 'CR2'), ('CR1', 'CR1'), ('PAST', 'PAST'), ('PR2', 'PR2'), ('PR1', 'PR1'), ('PRCE1', 'PRCE1'), ('PRCE2', 'PRCE2'), ('DR2', 'DR2'), ('DR1', 'DR1'), ('DRE', 'DRE'), ('AT', 'AT'), ('ATP', 'ATP'), ('ADJENES', 'ADJENES'), ('TCN', 'TCN'), ('TCS', 'TCS'), ('TCE', 'TCE'), ('SAENES', 'SAENES'), ('AI', 'AI'), ('IE', 'IE'), ('IR', 'IR')], max_length=50),
        ),
        migrations.AlterField(
            model_name='membrenew',
            name='nature_poste',
            field=models.CharField(null=True, blank=True, choices=[('CH', 'CH'), ('DOCT', 'DOCT'), ('EC', 'EC'), ('ENS', 'ENS'), ('ING', 'ING'), ('ITA', 'ITA'), ('VIS', 'VIS')], max_length=50),
        ),
        migrations.AlterField(
            model_name='membrenew',
            name='position',
            field=models.CharField(null=True, blank=True, choices=[('activité', 'activité'), ('associé', 'associé'), ('CDD', 'CDD'), ('décès', 'décès'), ('détachement', 'détachement'), ('disponibilité', 'disponibilité'), ('émerite', 'émérite'), ('parti', 'parti'), ('retraité', 'retraité')], max_length=50),
        ),
    ]
