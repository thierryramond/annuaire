# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annuaire', '0018_auto_20151017_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='membrenew',
            name='cn',
            field=models.CharField(choices=[(None, 'sans objet'), ('41', '41')], null=True, max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='membrenew',
            name='equipe',
            field=models.CharField(choices=[('AGA', 'AGA'), ('AH', 'AH'), ('ANEDP', 'ANEDP'), ('PS', 'PS'), ('TOPO', 'TOPO'), ('SE', 'SE')], null=True, max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='membrenew',
            name='grade',
            field=models.CharField(choices=[('POSTDOC', 'POSTDOC'), ('ATER', 'ATER'), ('CDD ATER', 'CDD ATER'), ('PRAG', 'PRAG'), ('MC', 'MC'), ('MC HC', 'MC HC'), ('CR2', 'CR2'), ('CR1', 'CR1'), ('PAST', 'PAST'), ('PR2', 'PR2'), ('PR1', 'PR1'), ('PRCE1', 'PRCE1'), ('PRCE2', 'PRCE2'), ('DR2', 'DR2'), ('DR1', 'DR1'), ('DRE', 'DRE'), ('AT', 'AT'), ('ATP', 'ATP'), ('ADJENES', 'ADJENES'), ('TCN', 'TCN'), ('TCS', 'TCS'), ('TCE', 'TCE'), ('SAENES', 'SAENES'), ('AI', 'AI'), ('IE', 'IE'), ('IR', 'IR')], null=True, max_length=50, blank=True),
        ),
    ]
