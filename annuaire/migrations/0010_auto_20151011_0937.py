# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annuaire', '0009_auto_20151010_1743'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='membre',
            options={'ordering': ('nom', 'prenom')},
        ),
        migrations.AlterField(
            model_name='membre',
            name='depart',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='membre',
            name='entree',
            field=models.DateField(null=True, blank=True),
        ),
    ]
