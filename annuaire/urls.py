"""annuaire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from annuaire.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^$', HomeView.as_view(), name='home'),
    url(r'^home/$', HomeView.as_view(), name='home'),
    url(r'^listeold/$',login_required(MembreOldList.as_view()),name='listeold'),
    url(r'^listenew/$',login_required(MembreNewList.as_view()),name='listenew'),
    url(r'^membrenew_update/(?P<pk>\d+)/$',login_required(MembreNewUpdate.as_view()),name='update'),
    url(r'^nettoyage/$','annuaire.views.nettoyage_quotite',name='nettoyage'),
    url(r'^import/$','annuaire.views.activite_doct',name='import'),
    url(r'^nouveau/$', login_required(MembreNewCreate.as_view()), name='create'),
    url(r'^delete/(?P<pk>\d+)$', login_required(MembreNewDelete.as_view()), name='delete'),
    url(r'^connexion/$', ConnexionView.as_view(), name='connexion'),
    url(r'^deconnexion/$', 'annuaire.views.deconnexion', name='deconnexion'),
]
