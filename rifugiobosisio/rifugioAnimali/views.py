from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from .models import Animale, ModuloAdozione
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from .filters import AnimaleFilter, AnimaleAdminFilter, ModuloAdozioneFilter

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

    #controllo se admin
    if(request.user.is_staff):
        return redirect('home_admin')
    
    lista_animali = Animale.objects.order_by("specie")
    lista_filtrata = AnimaleFilter(request.GET, queryset=lista_animali)
    template = loader.get_template("rifugioAnimali/home.html")
    context = {
        "lista_animali" : lista_animali,
        "lista_filtrata" : lista_filtrata,
    }
    return HttpResponse(template.render(context,request))

@login_required(login_url='login')
def home_admin(request):

    #controllo se admin
    if(not(request.user.is_staff)):
        return redirect('home')

    lista_moduli = ModuloAdozione.objects.order_by("animale")
    lista_filtrata = ModuloAdozioneFilter(request.GET, queryset=lista_moduli)
    template = loader.get_template("rifugioAnimali/home_amministratore.html")
    
    context = {
        "lista_moduli" : lista_moduli,
        "lista_filtrata" : lista_filtrata,
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

@login_required(login_url='login')
def logOut(request):
    username = request.user.username
    if username != None:
        logout(request)
        return redirect("/login")

@login_required(login_url='login')
def modulo_adozione(request,animali_id):
    animale_da_adottare = get_object_or_404(Animale, id=animali_id)
    if animale_da_adottare.stato == "ADOTTATO" or animale_da_adottare.stato == "IN_ATTESA":
        return redirect('home')
    
    if animale_da_adottare == None:
        return redirect('home')
    
    template = loader.get_template("rifugioAnimali/modulo_adozione.html")
    context = {
        "animale_da_adottare" : animale_da_adottare,
    }
    return HttpResponse(template.render(context,request))

@login_required(login_url='login')
def invio_modulo_adozione(request,animali_id):
    animale_da_adottare = get_object_or_404(Animale, id=animali_id)

    try:
        if request.POST["nomeCognome"] == "" or request.POST["indirizzo"] == "" or request.POST["recapito"] == "":
            raise KeyError
        if(animale_da_adottare.stato == "ADOTTATO" or animale_da_adottare.stato == "IN_ATTESA"):
            return redirect('home')
        nuovo_modulo = ModuloAdozione(nomeCognome = request.POST["nomeCognome"],indirizzo = request.POST["indirizzo"],recapito = request.POST["recapito"],animale = animale_da_adottare) #todo:cambiare con id utente loggato
        nuovo_modulo.save()

        

        animale_da_adottare.stato = "IN_ATTESA"
        animale_da_adottare.save()
    except (KeyError, ModuloAdozione.DoesNotExist):
        return render(request, "rifugioAnimali/modulo_adozione.html", {
            "animale_da_adottare" : animale_da_adottare,
            "error_message" : "Non hai compilato tutti i campi",
        })

    return redirect('home')


@login_required(login_url='login')
def gestione_animali(request):

    #controllo se admin
    if(not(request.user.is_staff)):
        return redirect('home')
    
    lista_animali = Animale.objects.order_by("specie")
    lista_filtrata = AnimaleAdminFilter(request.GET, queryset=lista_animali)
    template = loader.get_template("rifugioAnimali/gestione_animali.html")
    context = {
        "lista_animali" : lista_animali,
        "lista_filtrata" : lista_filtrata,
    }
    return HttpResponse(template.render(context,request))

@login_required(login_url='login')
def aggiungi_animale(request):
    #controllo se admin
    if(not(request.user.is_staff)):
        return redirect('home')
    
    template = loader.get_template("rifugioAnimali/aggiungi_animale.html")
    context = {}
    return HttpResponse(template.render(context,request))

@login_required(login_url='login')
def invio_aggiungi_animale(request):

    #controllo se admin
    if(not(request.user.is_staff)):
        return redirect('home')
    

    try:
        if request.POST["specie"] == "" or request.POST["razza"] == "" or request.POST["eta"] == "" :
            raise KeyError
        nuovo_animale = Animale(specie = request.POST["specie"],razza = request.POST["razza"],eta = request.POST["eta"],descrizione = request.POST["descrizione"],stato = 'NON_ADOTTATO')
        nuovo_animale.save()
    except (KeyError, Animale.DoesNotExist):
        return render(request, "rifugioAnimali/aggiungi_animale.html", {
            "error_message" : "Non hai compilato tutti i campi",
        })

    return redirect('gestione_animali')


@login_required(login_url='login')
def gestione_modulo_adozione(request,modulo_id,stato):
    #controllo se admin
    if(not(request.user.is_staff)):
        return redirect('home')
    
    modulo_da_gestire = ModuloAdozione.objects.get(id=modulo_id)
    try:
        if stato == "1":
            modulo_da_gestire.animale.stato = "ADOTTATO"
            modulo_da_gestire.full_clean()
            modulo_da_gestire.animale.save()
            msg = "Richiesta accettata con successo"
        elif stato == "0":
            modulo_da_gestire.animale.stato = "NON_ADOTTATO"
            modulo_da_gestire.animale.save()
            msg = "Richiesta rifiutata con successo"
        else:
            raise KeyError
    except (KeyError, ModuloAdozione.DoesNotExist):
        msg = "Errore nella gestione della richiesta"
        return redirect('home_admin')
    
    modulo_da_gestire.delete()
    return redirect('home_admin')

    



