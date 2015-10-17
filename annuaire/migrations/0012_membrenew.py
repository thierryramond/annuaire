# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('annuaire', '0011_auto_20151011_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='MembreNew',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('civilite', models.CharField(null=True, blank=True, max_length=10, choices=[('None', '----'), ('M.', 'M.'), ('Mme', 'Mme')])),
                ('nom', models.CharField(null=True, max_length=50, blank=True)),
                ('prenom', models.CharField(null=True, max_length=50, blank=True)),
                ('photo_url', models.URLField(null=True, blank=True)),
                ('mail', models.EmailField(null=True, max_length=254, blank=True)),
                ('tel', models.CharField(null=True, max_length=20, blank=True)),
                ('fax', models.CharField(null=True, max_length=20, blank=True)),
                ('web', models.URLField(null=True, blank=True)),
                ('batiment', models.CharField(null=True, blank=True, max_length=10, choices=[('None', '----'), ('425', '425'), ('430', '430'), ('440', '440'), ('IMO', 'IMO')])),
                ('bureau', models.CharField(null=True, max_length=10, blank=True)),
                ('position', models.CharField(null=True, blank=True, max_length=50, choices=[('None', '----'), ('en activité', 'en activité'), ('émerite', 'émerite'), ('associé', 'associé'), ('retraité', 'retraité'), ('promu', 'promu'), ('a muté', 'a muté'), ('décès', 'décès')])),
                ('nature_poste', models.CharField(null=True, blank=True, max_length=50, choices=[('None', '----'), ('chercheur', 'chercheur'), ('doctorant', 'doctorant'), ('enseignant-chercheur', 'enseignant-chercheur'), ('ITA', 'ITA')])),
                ('tutelle', models.CharField(null=True, max_length=50, blank=True)),
                ('grade', models.CharField(null=True, blank=True, max_length=50, choices=[('None', '----'), ('Post-Doc', 'Post-Doc'), ('ATER', 'ATER'), ('MC', 'MC'), ('MC HC', 'MC HC'), ('CR2', 'CR2'), ('CR1', 'CR1'), ('PR2', 'PR2'), ('PR1', 'PR1'), ('PRCE', 'PRCE'), ('DR2', 'DR2'), ('DR1', 'DR1'), ('DRE', 'DRE'), ('A', 'A'), ('T', 'T'), ('I', 'I')])),
                ('habilitation', models.CharField(null=True, blank=True, max_length=10, choices=[('None', '----'), ('oui', 'oui'), ('non', 'non')])),
                ('entree', models.DateField(null=True, blank=True)),
                ('depart', models.DateField(null=True, blank=True)),
                ('bap', models.CharField(null=True, blank=True, max_length=5, choices=[('None', '----'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J')])),
                ('directeur_these', models.CharField(null=True, max_length=50, blank=True)),
                ('annee_soutenance', models.CharField(null=True, max_length=20, blank=True)),
                ('mots_cles', models.CharField(null=True, max_length=255, blank=True)),
                ('liste_rouge', models.CharField(null=True, blank=True, max_length=10, choices=[('None', '----'), ('oui', 'oui'), ('non', 'non')])),
                ('cree_le', models.DateTimeField(auto_now_add=True)),
                ('modifie_le', models.DateTimeField(auto_now=True)),
                ('cree_par', models.ForeignKey(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
                ('modifie_par', models.ForeignKey(verbose_name='Modifié par', null=True, related_name='membrenew_mod', blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('nom', 'prenom'),
            },
        ),
    ]
