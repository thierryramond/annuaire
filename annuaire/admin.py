from django.contrib import admin
from annuaire.models import *
# Register your models here.

class MembreNewAdmin(admin.ModelAdmin):
	list_display 	= ('prenom','nom','bureau','batiment','position','nature_poste','grade')
	ordering 		= ('nom','prenom')

admin.site.register(MembreNew,MembreNewAdmin)