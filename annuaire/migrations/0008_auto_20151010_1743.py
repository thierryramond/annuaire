# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annuaire', '0007_auto_20151009_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membre',
            name='id',
            field=models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True),
        ),
        migrations.AlterField(
            model_name='membre',
            name='mail',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='membre',
            name='pageperso',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='membre',
            name='url_photo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
