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