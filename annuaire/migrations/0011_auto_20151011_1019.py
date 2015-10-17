# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annuaire', '0010_auto_20151011_0937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membre',
            old_name='these',
            new_name='directeur_these',
        ),
        migrations.AlterField(
            model_name='membre',
            name='listrouge',
            field=models.CharField(blank=True, null=True, max_length=10),
        ),
    ]
