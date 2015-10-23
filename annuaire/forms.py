from django import forms

from annuaire.models import *

class MembreForm(forms.ModelForm):
	class Meta:
		model = Membre
		fields= '__all__'

class MembreNewForm(forms.ModelForm):
	class Meta:
		model = MembreNew
		fields=('nom','prenom','date_naissance','bureau','batiment','position','nature_poste','grade','quotite')
		#exclude =('cree_le','cree_par','modifie_le','modifie_par')


class MembreNewFormComplet(forms.ModelForm):
	class Meta:
		model = MembreNew
		exclude =('cree_le','cree_par','modifie_le','modifie_par')


class ConnexionForm(forms.Form):
	username 		= forms.CharField(label="Nom d'utilisateur")
	password 		= forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

