"""
URL configuration for rifugiobosisio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_view
from django.urls import path,include
from rifugioAnimali import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/",include("django.contrib.auth.urls")),
    path("",views.home,name="home"),
    path("home/",views.home,name="home"),
    path("home_admin/",views.home_admin,name="home_admin"),
    path("login/",views.logIn,name="login"),
    path("logout/",views.logOut,name="logout"),
    path("registrazione/",views.registerPage,name="registrazione"),
    path("modulo_adozione/<int:animali_id>/",views.modulo_adozione,name="modulo_adozione"),
    path("invio_modulo_adozione/<int:animali_id>",views.invio_modulo_adozione,name="invio_modulo_adozione"),
    path("gestione_animali/",views.gestione_animali,name="gestione_animali"),
    path("aggiungi_animale/",views.aggiungi_animale,name="aggiungi_animale"),
    path("invio_aggiungi_animale/",views.invio_aggiungi_animale,name="invio_aggiungi_animale"),
    path("gestione_modulo_adozione/<modulo_id>/<stato>/",views.gestione_modulo_adozione,name="gestione_modulo_adozione"),
]