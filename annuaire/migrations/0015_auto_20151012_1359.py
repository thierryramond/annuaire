# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annuaire', '0014_auto_20151012_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='membrenew',
            name='cnu',
            field=models.CharField(max_length=10, null=True, blank=True, choices=[(None, 'sans objet'), ('25', '25'), ('26', '26')]),
        ),
        migrations.AlterField(
            model_name='membrenew',
            name='grade',
            field=models.CharField(max_length=50, null=True, blank=True, choices=[(None, 'sans objet'), ('POSTDOC', 'POSTDOC'), ('ATER', 'ATER'), ('MC', 'MC'), ('MC HC', 'MC HC'), ('CR2', 'CR2'), ('CR1', 'CR1'), ('PR2', 'PR2'), ('PR1', 'PR1'), ('PRCE1', 'PRCE1'), ('PRCE2', 'PRCE2'), ('DR2', 'DR2'), ('DR1', 'DR1'), ('DRE', 'DRE'), ('C FAC', 'C FAC'), ('TCN', 'TCN'), ('TCS', 'TCS'), ('TCE', 'TCE'), ('AI', 'AI'), ('IE', 'IE'), ('IR', 'IR')]),
        ),
    ]
