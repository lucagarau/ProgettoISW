
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django.utils.translation import gettext_lazy as _
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']
        labels = {
            'first_name': _('Nome'),
            'last_name': _('Cognome'),
            'username': _('Username'),
            'email': _('Email'),
            'password1': _('Password'),
            'password2': _('Conferma Password'),
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control me-2'}),
            'last_name': forms.TextInput(attrs={'class':'form-control me-2'}),
            'username': forms.TextInput(attrs={'class':'form-control me-2'}),
            'email': forms.EmailInput(attrs={'class':'form-control me-2'}),
            'password1': forms.PasswordInput(attrs={'class':'form-control me-2'}),
            'password2': forms.PasswordInput(attrs={'class':'form-control me-2'}),
        }

        