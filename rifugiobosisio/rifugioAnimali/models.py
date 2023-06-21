from random import choice
from django.db import models
from enum import Enum

#classe per il personale del rifugio di animali
class Utente(models.Model):
    nome = models.CharField(max_length = 32)
    cognome = models.CharField(max_length = 32)
    username = models.CharField(max_length = 64)
    password = models.CharField(max_length = 32)
    email = models.EmailField(max_length = 128) #se admin true allora è null
    lavoro = models.CharField(max_length = 64) # se admin true allora è null
    codiceImpiegato = models.IntegerField(default = 0) #se admin false allora è null
    admin = models.BooleanField()

    def __str__(self):
        return self.nome + self.cognome + self.username + self.password + self.email + str(self.codiceImpiegato) + self.admin


class StatoAdozione(Enum):
    ADOTTATO = 'adottato'
    NON_ADOTTATO = 'non adottato'
    IN_ATTESA = 'in attesa di conferma'
    
class Animale(models.Model):
    specie = models.CharField(max_length = 32)
    razza = models.CharField(max_length = 32)
    eta = models.IntegerField(default = 0)
    descrizione = models.CharField(max_length = 128)
    stato = models.CharField(max_length=32,choices=[(choice.name,choice.value) for choice in StatoAdozione],default=StatoAdozione.NON_ADOTTATO.value)

    def __str__(self):
        return self.specie + self.razza + str(self.eta) + self.descrizione

class ModuloAdozione(models.Model):
    nomeCognome = models.CharField(max_length = 64)
    indirizzo = models.CharField(max_length = 128)
    recapito = models.CharField(max_length = 128)
    animale = models.ForeignKey(Animale, on_delete = models.CASCADE)
    richiedente = models.ForeignKey(Utente, on_delete = models.CASCADE)

    def __str__(self):
        return self.nomeCognome + self.indirizzo + self.recapito