# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annuaire', '0006_membre_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membre',
            name='listrouge',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
