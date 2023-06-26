from random import choice
from typing import Any
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from enum import Enum
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator

def validate_nonempty_string(value):
    if not value.strip():
        raise ValidationError("Il valore non può essere una stringa vuota o contenente solo spazi vuoti.") 
    
class StatoAdozione(Enum):
    ADOTTATO = 'adottato'
    NON_ADOTTATO = 'non adottato'
    IN_ATTESA = 'in attesa di conferma'
    
class Animale(models.Model):
    specie = models.CharField(max_length = 32,blank=False,null=False,validators=[validate_nonempty_string])
    razza = models.CharField(max_length = 32,blank=False,null=False,validators=[validate_nonempty_string])
    eta = models.IntegerField(default = 0,blank=False,null=False,validators=[MinValueValidator(0)])
    descrizione = models.CharField(max_length = 128,blank=True)
    stato = models.CharField(max_length=32,choices=[(choice.name,choice.value) for choice in StatoAdozione],default=StatoAdozione.NON_ADOTTATO.value,blank=False,null=False,validators=[validate_nonempty_string])

    def __str__(self):
        return self.specie + " " + self.razza + " " + str(self.eta) + " " + self.descrizione + " " + self.stato


class ModuloAdozione(models.Model):
    nomeCognome = models.CharField(max_length = 64,blank=False,null=False,validators=[validate_nonempty_string])
    indirizzo = models.CharField(max_length = 128,blank=False,null=False,validators=[validate_nonempty_string])
    recapito = models.CharField(max_length = 128,blank=False,null=False,validators=[validate_nonempty_string])
    animale = models.ForeignKey(Animale, on_delete = models.CASCADE)

    def __str__(self):
        return self.nomeCognome + " " + self.indirizzo + " " + self.recapito + " " + str(self.animale)
