import django_filters
from django import forms
from django.utils.translation import gettext_lazy as _

class AnimaleFilter(django_filters.FilterSet):
    specie = django_filters.CharFilter(lookup_expr='icontains',label="specie", max_length=100, required=False,widget=forms.TextInput(attrs={'class':'form-control me-2'}))
    eta = django_filters.NumberFilter(label="età uguale a", required=False,widget=forms.TextInput(attrs={'class':'form-control me-2'}))
    eta_lt = django_filters.NumberFilter(field_name='eta', lookup_expr='lt',label="età minore di", required=False,widget=forms.TextInput(attrs={'class':'form-control me-2'}))
    eta_gt = django_filters.NumberFilter(field_name='eta', lookup_expr='gt',label="età maggiore di", required=False,widget=forms.TextInput(attrs={'class':'form-control me-2'}))
    razza = django_filters.CharFilter(lookup_expr='icontains',label="razza", max_length=100, required=False,widget=forms.TextInput(attrs={'class':'form-control me-2'}))

class AnimaleAdminFilter(django_filters.FilterSet):
    specie = django_filters.CharFilter(lookup_expr='icontains',label="specie", max_length=100, required=False,widget=forms.TextInput(attrs={'class':'form-control me-2'}))
    eta = django_filters.NumberFilter(label="età uguale a", required=False,widget=forms.TextInput(attrs={'class':'form-control me-2'}))
    eta_lt = django_filters.NumberFilter(field_name='eta', lookup_expr='lt',label="età minore di", required=False,widget=forms.TextInput(attrs={'class':'form-control me-2'}))
    eta_gt = django_filters.NumberFilter(field_name='eta', lookup_expr='gt',label="età maggiore di", required=False,widget=forms.TextInput(attrs={'class':'form-control me-2'}))
    razza = django_filters.CharFilter(lookup_expr='icontains',label="razza", max_length=100, required=False,widget=forms.TextInput(attrs={'class':'form-control me-2'}))
    stato = django_filters.ChoiceFilter(field_name="stato",choices=[('ADOTTATO','Adottato'),('IN_ATTESA','In Attesa'),('NON_ADOTTATO','Non Adottato')],label="stato adozione", required=False,widget=forms.Select(attrs={'class':'form-control me-2'}))

class ModuloAdozioneFilter(django_filters.FilterSet):
    nomeCognome = django_filters.CharFilter(lookup_expr='icontains',label="nome e cognome", max_length=100, required=False,widget=forms.TextInput(attrs={'class':'form-control me-2'}))
    indirizzo = django_filters.CharFilter(lookup_expr='icontains',label="indirizzo", max_length=100, required=False,widget=forms.TextInput(attrs={'class':'form-control me-2'}))
    recapito = django_filters.CharFilter(lookup_expr='icontains',label="recapito", max_length=100, required=False,widget=forms.TextInput(attrs={'class':'form-control me-2'}))
    #specie = django_filters.CharFilter(field_name='animale.specie',lookup_expr='icontains',label="specie animale", max_length=100, required=False,widget=forms.TextInput(attrs={'class':'form-control me-2'}))
    #eta = django_filters.NumberFilter(field_name='animale.eta',label="età animale uguale a", required=False,widget=forms.TextInput(attrs={'class':'form-control me-2'}))
    #eta_lt = django_filters.NumberFilter(field_name='animale.eta', lookup_expr='lt',label="età animale minore di", required=False,widget=forms.TextInput(attrs={'class':'form-control me-2'}))
    #eta_gt = django_filters.NumberFilter(field_name='animale.eta', lookup_expr='gt',label="età animale maggiore di", required=False,widget=forms.TextInput(attrs={'class':'form-control me-2'}))
    #razza = django_filters.CharFilter(field_name='animale.razza',lookup_expr='icontains',label="razza animale", max_length=100, required=False,widget=forms.TextInput(attrs={'class':'form-control me-2'}))