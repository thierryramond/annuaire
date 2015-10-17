# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annuaire', '0003_auto_20151009_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membre',
            name='motcles',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
