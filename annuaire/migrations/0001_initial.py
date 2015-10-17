# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('civilites', models.CharField(max_length=10)),
                ('nom', models.CharField(max_length=50)),
                ('nomjf', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('bat', models.CharField(max_length=50)),
                ('bureau', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=50)),
                ('fax', models.CharField(max_length=50)),
                ('mail', models.CharField(max_length=50)),
                ('pageperso', models.CharField(max_length=50)),
                ('equipes', models.CharField(max_length=50)),
                ('fonctions', models.CharField(max_length=50)),
                ('nouvellefonctions', models.CharField(max_length=50)),
                ('grades', models.CharField(max_length=50)),
                ('bap', models.CharField(max_length=50)),
                ('tutelle', models.CharField(max_length=50)),
                ('responsable', models.CharField(max_length=50)),
                ('cn', models.CharField(max_length=50)),
                ('cnu', models.CharField(max_length=50)),
                ('habilitation', models.CharField(max_length=50)),
                ('entree', models.CharField(max_length=50)),
                ('depart', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('annee', models.CharField(max_length=50)),
                ('these', models.CharField(max_length=50)),
                ('motcles', models.CharField(max_length=50)),
                ('listrouge', models.CharField(max_length=50)),
                ('url_photo', models.CharField(max_length=50)),
                ('membre_associe', models.CharField(max_length=50)),
                ('emeritat', models.CharField(max_length=50)),
            ],
        ),
    ]
