from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from .models import Animale, ModuloAdozione
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def registerPage(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form':form}
    template = loader.get_template("registration/registrazione.html")
    return HttpResponse(template.render(context,request))

@login_required(login_url='login')
def home(request):
    lista_animali = Animale.objects.order_by("specie")
    template = loader.get_template("rifugioAnimali/home.html")
    context = {
        "lista_animali" : lista_animali,
    }
    return HttpResponse(template.render(context,request))

@login_required(login_url='login')
def home_admin(request):
    #todo: mettere controllo se admin, altrimenti redirect a home
    lista_moduli = ModuloAdozione.objects.order_by("animale")
    template = loader.get_template("rifugioAnimali/home_amministratore.html")
    context = {
        "lista_moduli" : lista_moduli,
    }
    return HttpResponse(template.render(context,request))

def logIn(request):
    if request.method == 'POST':
        usr = request.POST.get('username')
        psw = request.POST.get('password')
        
        user = authenticate(request, username=usr, password=psw)

        if user is not None and not(user.is_staff):
            login(request, user)
            return redirect('home')
        elif user is not None and user.is_staff:
            login(request, user)
            return redirect('home_admin')

    template = loader.get_template("registration/login.html")
    return HttpResponse(template.render({},request))

def logOut(request):
    username = request.user.username
    if username != None:
        logout(request)
        return redirect("/login")

def modulo_adozione(request,animali_id):
    animale_da_adottare = Animale.objects.get(id=animali_id)
    template = loader.get_template("rifugioAnimali/modulo_adozione.html")
    context = {
        "animale_da_adottare" : animale_da_adottare,
    }
    return HttpResponse(template.render(context,request))

def invio_modulo_adozione(request,animali_id):
    animale_da_adottare = get_object_or_404(Animale, id=animali_id)

    #utente_loggato = Utente(nome = "gianni", cognome = "fenu", username = "gianni", password = "fenu", admin = False)
    #utente_loggato.save() #todo:cambiare con id utente loggato

    try:
        if request.POST["nomeCognome"] == "" or request.POST["indirizzo"] == "" or request.POST["recapito"] == "":
            raise KeyError
        nuovo_modulo = ModuloAdozione(nomeCognome = request.POST["nomeCognome"],indirizzo = request.POST["indirizzo"],recapito = request.POST["recapito"],animale = animale_da_adottare) #todo:cambiare con id utente loggato
        nuovo_modulo.save()
    except (KeyError, ModuloAdozione.DoesNotExist):
        return render(request, "rifugioAnimali/modulo_adozione.html", {
            "animale_da_adottare" : animale_da_adottare,
            "error_message" : "Non hai compilato tutti i campi",
        })

    template = loader.get_template("rifugioAnimali/home.html") #todo: cambiare con pagina di conferma
    context = {
        "animale_da_adottare" : animale_da_adottare,
    }
    return HttpResponse(template.render(context,request))



