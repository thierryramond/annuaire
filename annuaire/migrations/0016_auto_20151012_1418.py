# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annuaire', '0015_auto_20151012_1359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membrenew',
            name='quotité',
        ),
        migrations.AddField(
            model_name='membrenew',
            name='quotite',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
