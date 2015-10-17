from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse_lazy, reverse

from django.views.generic import View,TemplateView, FormView, ListView,\
		DetailView, CreateView, UpdateView, DeleteView

from datetime import datetime

from annuaire.forms import *


class HomeView(TemplateView):
	template_name = 'annuaire/home.html'
	titre = "Annuaire du DMO"

class MembreOldList(ListView):
	titre 			= "Liste des membres - Old"
	model 			= Membre
	template_name 	= 'annuaire/membreold_list.html'

class MembreNewList(ListView):
	titre 			= "Liste des membres - nouveau modèle"
	model 			= MembreNew
	template_name 	= 'annuaire/membrenew_list.html'

class MembreNewUpdate(UpdateView):
	titre = "Modifier un membre"
	model = MembreNew
	form_class = MembreNewForm
	template_name = 'annuaire/membrenew_update.html'
	

	def form_valid(self, form):
		form.instance.modif_par = self.request.user
		return super(MembreNewUpdate, self).form_valid(form)

	def get_success_url(self):
		return '/membrenew_update/%s/' %self.object.next().id


def nettoyage_depart(request):
	for membre in MembreNew.objects.all():
		if membre.depart:
			if membre.depart > datetime.today().date(): membre.depart = None
			membre.save()
	return redirect(reverse('listenew'))

def nettoyage_nom(request):
	for membre in Membre.objects.all():
		membre.nom = membre.nom.lower().capitalize()
		if membre.nomjf: membre.nomjf = membre.nomjf.lower().capitalize()
		membre.prenom = membre.prenom.lower().capitalize()
		membre.save()
	return redirect(reverse('liste'))

def nettoyage_grade(request):
	for membre in Membre.objects.all():
		if membre.grades == "NEANT": membre.grades=""
		membre.save()
	return redirect(reverse('liste'))


def nettoyage_telephone(request):
	for membre in Membre.objects.all():
		if membre.tel == "(+33) 1-69-15--" or membre.tel =="(+33) 1-69-15" or membre.tel =="(+33) 1-69-15-": membre.tel=""
		membre.save()
	return redirect(reverse('liste'))

def nettoyage_fax(request):
	for membre in MembreNew.objects.all():
		if membre.fax == "(+33) 1-69-15--" or membre.fax =="(+33) 1-69-15" or membre.fax =="(+33) 1-69-15-": membre.fax=""
		membre.save()
	return redirect(reverse('listenew'))

def nettoyage_bap(request):
	for membre in MembreNew.objects.all():
		if membre.bap =="NEANT": membre.bap=""
		if membre.nature_poste !="ITA": membre.bap=""
		membre.save()
	return redirect(reverse('listenew'))



def nettoyage_pageperso(request):
	for membre in Membre.objects.all():
		if membre.pageperso=="http://www.math.u-psud.fr/" or membre.pageperso=="http://www.math.u-psud.fr": membre.pageperso=""
		membre.save()
	return redirect(reverse('liste'))

def nettoyage_date(request):
	for membre in Membre.objects.all():
		if membre.entree : membre.entree = ""
		if membre.depart : membre.depart = ""
		if membre.entree : membre.entree = datetime.strptime(membre.entree, "%Y-%m-%d").date()
		if membre.depart : membre.depart=datetime.strptime(membre.depart, "%Y-%m-%d").date()
		membre.save()
	return redirect(reverse('liste'))

def nettoyage_bureau(request):
	for membre in MembreNew.objects.all():
		if membre.bureau == "000": membre.bureau=""
		if membre.batiment == "000": membre.batiment=""
		membre.save()
	return redirect(reverse('listenew'))

def importation(request):
	for membre in Membre.objects.all():
		membrenew = MembreNew(
			civilite 			= membre.civilites,
			nom 				= membre.nom,
			prenom 				= membre.prenom,
			photo_url			= membre.url_photo,
			mail 				= membre.mail,
			tel 				= membre.tel,
			fax 				= membre.fax,
			web 				= membre.pageperso,
			batiment 			= membre.bat,
			bureau 				= membre.bureau,
			equipe 				= membre.equipes,
			position 			= membre.position,
			nature_poste		= membre.fonctions,
			tutelle 			= membre.tutelle,
			grade 				= membre.grades,
			habilitation 		= membre.habilitation,
			entree 				= membre.entree,
			depart 				= membre.depart,
			bap 				= membre.bap,
			directeur_these 	= membre.directeur_these,
			annee_soutenance 	= membre.annee,
			mots_cles 			= membre.motcles,
			liste_rouge 		= membre.listrouge,
			)
		if membre.emeritat and membre.emeritat == 1 : membrenew.position = "émérite"
		membrenew.save()

	return redirect(reverse('listenew'))

def importation_nature(request):
	for membre in MembreNew.objects.all():
		membreold=Membre.objects.get(nom=membre.nom,prenom=membre.prenom)
		if 'EC' in membreold.fonctions:
			membre.nature_poste = 'EC'
		if 'CH' in membreold.fonctions:
			membre.nature_poste ='CH'
		if 'NEANT' in membreold.fonctions:
			membre.nature_poste = ''
		if membreold.fonctions == 'DOCT' :
			membre.nature_poste = 'DOCT'
		if membreold.fonctions == 'ADM'  or membreold.fonctions == 'AI':
			membre.nature_poste = 'ITA'
		if membreold.fonctions == 'ING' :
			membre.nature_poste = 'ITA'
		if membreold.fonctions == 'POSTDOC' :
			membre.nature_poste = 'POSTDOC'
		membre.save()
	return redirect(reverse('listenew'))


def nettoyage_grade(request):
	for membre in MembreNew.objects.all():
		if membre.grade: 
			if 'NEANT' in membre.grade:
				membre.grade = ''
			if membre.grade == 'PREMERIT':
				membre.grade ="Emérite"
			if membre.grade == 'STAG':
				membre.grade=''
			if membre.grade =='NONE':
				membre.grade=''
			if membre.nature_poste =='DOCT':
				membre.grade=''
		membre.save()
	return redirect(reverse('listenew'))


def nettoyage_position(request):
	for membre in MembreNew.objects.all():
		if membre.grade == "Emérite":
			membre.position = "Emérite"
		membre.save()
	return redirect(reverse('listenew'))


def activite(request):
	for membre in MembreNew.objects.all():
		if membre.position =="en activité" or membre.position =="activite":
			membre.position ="activité"
		membre.save()
	return redirect(reverse('listenew'))

def activite_doct(request):
	for membre in MembreNew.objects.all():
		if membre.nature_poste =="DOCT" and  membre.depart and membre.depart< datetime.today().date():
			membre.position ="parti"
		membre.save()
	return redirect(reverse('listenew'))



def nettoyage_tutelle(request):
	for membre in MembreNew.objects.all():
		if membre.tutelle == "Paris Sud" or membre.tutelle == "Paris 11" or membre.tutelle == "Université Paris-Sud"\
			or membre.tutelle =="Université Paris 11" or membre.tutelle =="Paris XI" or membre.tutelle =="Université Paris Sud XI"  \
			or membre.tutelle =="UniversitÃ© Paris Sud XI" or membre.tutelle == "UNIVERSITÉ PARIS-SUD":
			membre.tutelle ="Université Paris Sud"
		membre.save()
	return redirect(reverse('listenew'))

def nettoyage_quotite1(request):
	for membre in MembreNew.objects.all():
		membre.quotite="100"
		if membre.nature_poste == "DOCT": membre.quotite = None
		membre.save()
	return redirect(reverse('listenew'))


def nettoyage_emerite(request):
	for membre in MembreNew.objects.all():
		if membre.position == "émerite": membre.position = "émérite"
		membre.save()
	return redirect(reverse('listenew'))

def nettoyage_bureau_1(request):
	for membre in MembreNew.objects.all():
		if membre.position == "parti": 
			membre.bureau = None
			membre.batiment = None
		membre.save()
	return redirect(reverse('listenew'))

def nettoyage_bureau(request):
	for membre in MembreNew.objects.all():
		if membre.batiment == "Autre": 
			membre.bureau = None
			membre.batiment = None
		membre.save()
	return redirect(reverse('listenew'))

def nettoyage_quotite(request):
	for membre in MembreNew.objects.all():
		if membre.position == "parti": membre.quotite = None
		membre.save()
	return redirect(reverse('listenew'))


