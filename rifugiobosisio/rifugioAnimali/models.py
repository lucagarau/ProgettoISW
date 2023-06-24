from random import choice
from typing import Any
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from enum import Enum


    
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
        return self.specie + " " + self.razza + " " + str(self.eta) + " " + self.descrizione + " " + self.stato


class ModuloAdozione(models.Model):
    nomeCognome = models.CharField(max_length = 64)
    indirizzo = models.CharField(max_length = 128)
    recapito = models.CharField(max_length = 128)
    animale = models.ForeignKey(Animale, on_delete = models.CASCADE)

    def __str__(self):
        return self.nomeCognome + " " + self.indirizzo + " " + self.recapito + " " + str(self.animale)
