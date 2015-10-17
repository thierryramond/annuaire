from django.db import models
from django.contrib.auth.models import User

class Membre(models.Model):
	NUM					= models.CharField(max_length=10, null=True,blank=True)
	civilites 			= models.CharField(max_length=10, null=True,blank=True)
	nom 				= models.CharField(max_length=50, null=True,blank=True)
	nomjf 				= models.CharField(max_length=50, null=True,blank=True)
	prenom 				= models.CharField(max_length=50, null=True,blank=True)
	bat 				= models.CharField(max_length=50, null=True,blank=True)
	bureau 				= models.CharField(max_length=50, null=True,blank=True)
	tel 				= models.CharField(max_length=50, null=True,blank=True)
	fax 				= models.CharField(max_length=50, null=True,blank=True)
	mail 				= models.CharField(max_length=100, null=True,blank=True)
	pageperso 			= models.CharField(max_length=255, null=True,blank=True)
	equipes 			= models.CharField(max_length=50, null=True,blank=True)
	fonctions 			= models.CharField(max_length=50, null=True,blank=True)
	nouvellefonctions 	= models.CharField(max_length=50, null=True,blank=True)
	grades 				= models.CharField(max_length=50, null=True,blank=True)
	bap 				= models.CharField(max_length=50, null=True,blank=True)
	tutelle 			= models.CharField(max_length=50, null=True,blank=True)
	responsable 		= models.CharField(max_length=50, null=True,blank=True)
	cn 					= models.CharField(max_length=50, null=True,blank=True)
	cnu 				= models.CharField(max_length=50, null=True,blank=True)
	habilitation 		= models.CharField(max_length=50, null=True,blank=True)
	entree 				= models.DateField(null=True,blank=True)
	depart 				= models.DateField(null=True,blank=True)
	position 			= models.CharField(max_length=50, null=True,blank=True)
	annee 				= models.CharField(max_length=50, null=True,blank=True)
	directeur_these 	= models.CharField(max_length=255, null=True,blank=True)
	motcles 			= models.CharField(max_length=255, null=True,blank=True)
	listrouge 			= models.CharField(max_length=10, null=True,blank=True)
	url_photo 			= models.CharField(max_length=255, null=True,blank=True)
	membre_associe 		= models.CharField(max_length=50, null=True,blank=True)
	emeritat 			= models.CharField(max_length=50, null=True,blank=True)

	class Meta:
		ordering		= ('nom','prenom')

	def __str__(self):
		return self.nom

batiment_list 	= (
	('425','425'),
	('430','430'),
	('440','440'),
	('IMO','IMO'),
	)
civilite_list 	= (
	('M.','M.'),
	('Mme','Mme'),
	)

cnu_list =(
	(None,'sans objet'),
	('25','25'),
	('26','26'),
	)

position_list 	= (
	('activité','activité'),
	('associé','associé'),
	('CDD','CDD'),
	('décès','décès'),
	('détachement','détachement'),
	('disponibilité','disponibilité'),
	('émérite','émérite'),
	('parti','parti'),
	('retraité','retraité'),
	)

poste_list 		= (
	('CH','CH'),
	('DOCT','DOCT'),
	('EC','EC'),
	('ENS','ENS'),
	('ING','ING'),
	('ITA','ITA'),
	('VIS','VIS'),
	)
grade_list		= (
	(None,'sans objet'),
	('POSTDOC','POSTDOC'),
	('ATER','ATER'),
	('CDD ATER','CDD ATER'),
	('PRAG','PRAG'),
	('MC','MC'),
	('MC HC','MC HC'),
	('CR2','CR2'),
	('CR1','CR1'),
	('PAST','PAST'),
	('PR2','PR2'),
	('PR1','PR1'),
	('PRCE1','PRCE1'),
	('PRCE2','PRCE2'),
	('DR2','DR2'),
	('DR1','DR1'),
	('DRE','DRE'),
	('AT','AT'),
	('ATP','ATP'),
	('ADJENES','ADJENES'),
	('TCN','TCN'),
	('TCS','TCS'),
	('TCE','TCE'),
	('SAENES','SAENES'),
	('AI','AI'),
	('IE','IE'),
	('IR','IR'),
	)

bap_list 		= (
	(None,'sans objet'),
	('A','A'),
	('B','B'),
	('C','C'),
	('D','D'),
	('E','E'),
	('F','F'),
	('G','G'),
	('H','H'),
	('I','I'),
	('J','J'),
	)

ouinon_list 	= (
	('oui','oui'),
	('non','non'),
	)

class MembreNew(models.Model):
	civilite 			= models.CharField(max_length=10, null=True, blank=True,choices=civilite_list)
	nom 				= models.CharField(max_length=50, null=True, blank=True)
	prenom 				= models.CharField(max_length=50, null=True, blank=True)
	date_naissance 		= models.DateField(null=True,blank=True)
	photo_url 			= models.URLField(null=True, blank=True)
	mail 				= models.EmailField(null=True, blank=True)
	tel 				= models.CharField(max_length=20, null=True, blank=True)
	fax 				= models.CharField(max_length=20, null=True, blank=True)
	web 				= models.URLField(null=True,blank=True)
	batiment 			= models.CharField(max_length=10, null=True, blank=True, choices=batiment_list)
	bureau				= models.CharField(max_length=10, null=True, blank=True)
	equipe 				= models.CharField(max_length=50, null=True,blank=True)
	position			= models.CharField(max_length=50, null=True, blank=True, choices=position_list)
	quotite 			= models.IntegerField(null=True, blank=True,)
	nature_poste		= models.CharField(max_length=50, null=True, blank=True, choices=poste_list)
	tutelle 			= models.CharField(max_length=50, null=True, blank=True)
	cnu 				= models.CharField(max_length=10, null=True, blank=True, choices=cnu_list)
	grade 				= models.CharField(max_length=50, null=True, blank=True, choices=grade_list)
	habilitation 		= models.CharField(max_length=10, null=True, blank=True, choices=ouinon_list)
	entree 				= models.DateField(null=True,blank=True)
	depart 				= models.DateField(null=True,blank=True)
	bap 				= models.CharField(max_length=5, null=True, blank=True, choices=bap_list)
	directeur_these 	= models.CharField(max_length=50, null=True, blank=True)
	annee_soutenance 	= models.CharField(max_length=20, null=True, blank=True)
	mots_cles 			= models.CharField(max_length=255, null=True, blank=True)
	liste_rouge 		= models.CharField(max_length=10, null=True, blank=True, choices=ouinon_list)
	cree_le 			= models.DateTimeField(auto_now_add=True)
	cree_par 			= models.ForeignKey(User,null=True, blank=True)
	modifie_le 			= models.DateTimeField(auto_now=True)
	modifie_par 		= models.ForeignKey(User,null=True, blank=True,verbose_name="Modifié par", related_name='%(class)s_mod')


	class Meta:
		ordering		= ('nom','prenom')

	def __str__(self):
		return '{0} {1}'.format(self.civilite,self.nom)

	def next(self):
		try:
			return MembreNew.objects.get(pk=self.pk+1)
		except:
			return None

	def previous(self):
		try:
			return MembreNew.objects.get(pk=self.pk-1)
		except:
			return None


