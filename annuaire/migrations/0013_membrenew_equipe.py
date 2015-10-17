# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annuaire', '0012_membrenew'),
    ]

    operations = [
        migrations.AddField(
            model_name='membrenew',
            name='equipe',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
