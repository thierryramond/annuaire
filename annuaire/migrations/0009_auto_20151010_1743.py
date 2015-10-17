# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annuaire', '0008_auto_20151010_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membre',
            name='these',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
