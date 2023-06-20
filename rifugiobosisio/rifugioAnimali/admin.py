from django.contrib import admin
from .models import Utente,Animale,ModuloAdozione

admin.site.register(Animale)
admin.site.register(Utente)
admin.site.register(ModuloAdozione)

# Register your models here.
