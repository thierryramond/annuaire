# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annuaire', '0013_membrenew_equipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='membrenew',
            name='quotité',
            field=models.IntegerField(null=True, default='100', blank=True),
        ),
        migrations.AlterField(
            model_name='membrenew',
            name='bap',
            field=models.CharField(null=True, max_length=5, choices=[(None, 'sans objet'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J')], blank=True),
        ),
        migrations.AlterField(
            model_name='membrenew',
            name='batiment',
            field=models.CharField(null=True, max_length=10, choices=[('425', '425'), ('430', '430'), ('440', '440'), ('IMO', 'IMO')], blank=True),
        ),
        migrations.AlterField(
            model_name='membrenew',
            name='civilite',
            field=models.CharField(null=True, max_length=10, choices=[('M.', 'M.'), ('Mme', 'Mme')], blank=True),
        ),
        migrations.AlterField(
            model_name='membrenew',
            name='grade',
            field=models.CharField(null=True, max_length=50, choices=[(None, 'sans objet'), ('POSTDOC', 'POSTDOC'), ('ATER', 'ATER'), ('MC', 'MC'), ('MC HC', 'MC HC'), ('CR2', 'CR2'), ('CR1', 'CR1'), ('PR2', 'PR2'), ('PR1', 'PR1'), ('PRCE1', 'PRCE1'), ('PRCE2', 'PRCE2'), ('DR2', 'DR2'), ('DR1', 'DR1'), ('DRE', 'DRE'), ('TCN', 'TCN'), ('TCS', 'TCS'), ('TCE', 'TCE'), ('A', 'A'), ('T', 'T'), ('I', 'I')], blank=True),
        ),
        migrations.AlterField(
            model_name='membrenew',
            name='habilitation',
            field=models.CharField(null=True, max_length=10, choices=[('oui', 'oui'), ('non', 'non')], blank=True),
        ),
        migrations.AlterField(
            model_name='membrenew',
            name='liste_rouge',
            field=models.CharField(null=True, max_length=10, choices=[('oui', 'oui'), ('non', 'non')], blank=True),
        ),
        migrations.AlterField(
            model_name='membrenew',
            name='nature_poste',
            field=models.CharField(null=True, max_length=50, choices=[('CH', 'CH'), ('DOCT', 'DOCT'), ('EC', 'EC'), ('ITA', 'ITA')], blank=True),
        ),
        migrations.AlterField(
            model_name='membrenew',
            name='position',
            field=models.CharField(null=True, max_length=50, choices=[('en activité', 'en activité'), ('CDD', 'CDD'), ('émerite', 'émérite'), ('associé(e)', 'associé(e)'), ('détaché(e)', 'détaché(e)'), ('disponibilité', 'disponibilité'), ('retraité(e)', 'retraité(e)'), ('promu(e)', 'promu(e)'), ('a muté', 'a muté'), ('décès', 'décès')], blank=True),
        ),
    ]
