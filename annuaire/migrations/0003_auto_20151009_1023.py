# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annuaire', '0002_auto_20151009_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membre',
            name='NUM',
            field=models.CharField(null=True, max_length=10, blank=True),
        ),
    ]
