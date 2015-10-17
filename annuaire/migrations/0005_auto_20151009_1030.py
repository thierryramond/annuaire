# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annuaire', '0004_auto_20151009_1027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membre',
            name='NUM',
        ),
        migrations.AlterField(
            model_name='membre',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
