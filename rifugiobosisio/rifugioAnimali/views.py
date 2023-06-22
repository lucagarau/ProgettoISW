from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Animale

# Create your views here.

def home(request):
    lista_animali = Animale.objects.order_by("specie")
    template = loader.get_template("rifugioAnimali/home.html")
    context = {
        "lista_animali" : lista_animali,
    }
    return HttpResponse(template.render(context,request))

def login(request):
    template = loader.get_template("registrazione/login.html")
    return HttpResponse(template.render({},request))

def modulo_adozione(request,animali_id):
    animale_da_adottare = Animale.objects.get(id=animali_id)
    template = loader.get_template("rifugioAnimali/modulo_adozione.html")
    context = {
        "animale_da_adottare" : animale_da_adottare,
    }
    return HttpResponse(template.render(context,request))