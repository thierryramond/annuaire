# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annuaire', '0005_auto_20151009_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='membre',
            name='NUM',
            field=models.CharField(null=True, blank=True, max_length=10),
        ),
    ]
