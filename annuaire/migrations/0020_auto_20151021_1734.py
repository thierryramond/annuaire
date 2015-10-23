# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annuaire', '0019_auto_20151019_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membrenew',
            name='bap',
            field=models.CharField(max_length=5, null=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J')], blank=True),
        ),
        migrations.AlterField(
            model_name='membrenew',
            name='cn',
            field=models.CharField(max_length=10, null=True, choices=[('41', '41')], blank=True),
        ),
        migrations.AlterField(
            model_name='membrenew',
            name='cnu',
            field=models.CharField(max_length=10, null=True, choices=[('25', '25'), ('26', '26')], blank=True),
        ),
    ]
