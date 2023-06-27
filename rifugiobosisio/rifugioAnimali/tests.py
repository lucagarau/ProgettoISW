from django.test import TestCase
from .models import Animale, ModuloAdozione
from django.contrib.auth.models import User
from .views import registerPage, home, home_admin, logIn
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from django.urls import reverse

'''
-----------------------------------------------------------------
TEST UNITARI PER MODELS.PY
-----------------------------------------------------------------

'''

'''
    Test Unitari per la classe Animale:
    - Test per il corretto inserimento dei campi
    - Test per la non unicità dell'id
    - Test per la non vuotezza dei campi specie e razza
    - Test per la non vuotezza del campo eta
    - Test per la non negatività del campo eta
    - Test per la vuotezza del campo descrizione
    - Test per la non vuotezza del campo stato
    - Test per la verifica della validità dello stato
'''
class AnimaleTestCase(TestCase):
    def setUp(self):
        Animale.objects.create(id=100,specie="cane",razza="pastore tedesco",eta=5,descrizione="cane di 5 anni",stato="non adottato")
    
    def test_animali_specie_field(self):
        cane = Animale.objects.get(id=100)
        self.assertEqual(cane.specie,"cane")
    
    def test_animali_razza_field(self):
        cane = Animale.objects.get(id=100)
        self.assertEqual(cane.razza,"pastore tedesco")

    def test_animali_eta_field(self):
        cane = Animale.objects.get(id=100)
        self.assertEqual(cane.eta,5)

    def test_animali_descrizione_field(self):
        cane = Animale.objects.get(id=100)
        self.assertEqual(cane.descrizione,"cane di 5 anni")

    def test_animali_stato_field(self):
        cane = Animale.objects.get(id=100)
        self.assertEqual(cane.stato,"non adottato")

    def test_animali_not_unique(self):
        with self.assertRaises(IntegrityError):
            Animale.objects.create(id=100,specie="cane",razza="pastore tedesco",eta=5,descrizione="cane di 5 anni",stato="non adottato")
    
    def test_animali_specie_field_not_empty(self):
        with self.assertRaises(ValidationError):
            Animale.objects.create(id=101,specie="",razza="pastore tedesco",eta=5,descrizione="cane di 5 anni",stato="non adottato").full_clean()

    def test_animali_razza_field_not_empty(self):
        with self.assertRaises(ValidationError):
            Animale.objects.create(id=101,specie="cane",razza="",eta=5,descrizione="cane di 5 anni",stato="non adottato").full_clean()

    def test_animali_eta_field_not_empty(self):
        with self.assertRaises(IntegrityError):
            Animale.objects.create(id=101,specie="cane",razza="pastore tedesco",eta=None,descrizione="cane di 5 anni",stato="non adottato").full_clean()

    def test_animali_eta_lower_than_0(self):
        with self.assertRaises(ValidationError):
            Animale.objects.create(id=101,specie="cane",razza="pastore tedesco",eta=-1,descrizione="cane di 5 anni",stato="non adottato").full_clean()

    def test_animali_descrizione_field_empty(self):
        animale = Animale.objects.create(id=101,specie="cane",razza="pastore tedesco",eta=5,descrizione="",stato="non adottato")
        self.assertEqual(animale.descrizione,"")

    def test_animali_stato_field_not_empty(self):
        with self.assertRaises(ValidationError):
            Animale.objects.create(id=101,specie="cane",razza="pastore tedesco",eta=5,descrizione="cane di 5 anni",stato="").full_clean()

    def test_animali_stato_field_not_valid(self):
        with self.assertRaises(ValidationError):
            Animale.objects.create(id=101,specie="cane",razza="pastore tedesco",eta=5,descrizione="cane di 5 anni",stato="stato non valido").full_clean()

    

      
'''
    Test Unitari per la classe ModuloAdozione:
    - Test per il corretto inserimento dei campi
    - Test per la non unicità dell'id
    - Test per la non vuotezza dei campi nomeCognome, indirizzo e recapito
    - Test per la non vuotezza del campo animale
    - Test per la verifica della validità dell'animale
'''
class ModuloAdozioneTestCase(TestCase):
    def setUp(self):
        Animale.objects.create(id=100,specie="cane",razza="pastore tedesco",eta=5,descrizione="cane di 5 anni",stato="non adottato")
        ModuloAdozione.objects.create(id=100,nomeCognome="Mario Rossi",indirizzo="via roma 1",recapito="123456789",animale=Animale.objects.get(id=100))
    
    def test_modulo_adozione_nomeCognome_field(self):
        modulo = ModuloAdozione.objects.get(id=100)
        self.assertEqual(modulo.nomeCognome,"Mario Rossi")
    
    def test_modulo_adozione_indirizzo_field(self):
        modulo = ModuloAdozione.objects.get(id=100)
        self.assertEqual(modulo.indirizzo,"via roma 1")

    def test_modulo_adozione_recapito_field(self):
        modulo = ModuloAdozione.objects.get(id=100)
        self.assertEqual(modulo.recapito,"123456789")

    def test_modulo_adozione_animale_field_dont_exist(self):
        with self.assertRaises(Animale.DoesNotExist):
            ModuloAdozione.objects.create(id=101,nomeCognome="Mario Rossi",indirizzo="via roma 1",recapito="123456789",animale=Animale.objects.get(id=101))

    def test_modulo_adozione_animale_field(self):
        modulo = ModuloAdozione.objects.get(id=100)
        self.assertEqual(modulo.animale,Animale.objects.get(id=100))

    def test_modulo_not_unique(self):
        with self.assertRaises(IntegrityError):
            ModuloAdozione.objects.create(id=100,nomeCognome="Mario Rossi",indirizzo="via roma 1",recapito="123456789",animale=Animale.objects.get(id=100))
    
    def test_modulo_adozione_animale_field_not_null(self):
        with self.assertRaises(IntegrityError):
            ModuloAdozione.objects.create(id=101,nomeCognome="Mario Rossi",indirizzo="via roma 1",recapito="123456789",animale=None)

    def test_modulo_adozione_nomeCognome_field_not_null(self):
        with self.assertRaises(IntegrityError):
            ModuloAdozione.objects.create(id=101,nomeCognome=None,indirizzo="via roma 1",recapito="123456789",animale=Animale.objects.get(id=100))

    def test_modulo_adozione_indirizzo_field_not_null(self):
        with self.assertRaises(IntegrityError):
            ModuloAdozione.objects.create(id=101,nomeCognome="Mario Rossi",indirizzo=None,recapito="123456789",animale=Animale.objects.get(id=100))
    
    def test_modulo_adozione_recapito_field_not_null(self):
        with self.assertRaises(IntegrityError):
            ModuloAdozione.objects.create(id=101,nomeCognome="Mario Rossi",indirizzo="via roma 1",recapito=None,animale=Animale.objects.get(id=100))

    def test_modulo_adozione_nomeCognome_field_blank(self):
        with self.assertRaises(ValidationError):
            ModuloAdozione.objects.create(id=101,nomeCognome="",indirizzo="cia roma 1",recapito="123456789",animale=Animale.objects.get(id=100)).full_clean()

    def test_modulo_adozione_indirizzo_field_blank(self):
        with self.assertRaises(ValidationError):
            ModuloAdozione.objects.create(id=101,nomeCognome="Mario Rossi",indirizzo=" ",recapito="123456789",animale=Animale.objects.get(id=100)).full_clean()

    def test_modulo_adozione_recapito_field_blank(self):
        with self.assertRaises(ValidationError):
            ModuloAdozione.objects.create(id=101,nomeCognome="Mario Rossi",indirizzo="via roma 1",recapito="",animale=Animale.objects.get(id=100)).full_clean()
    

'''
---------------------------------------------------------------------------------
 TEST UNITARI PER LE VISTE
---------------------------------------------------------------------------------
'''

'''
    Test Unitari per la view login :
    - Test per il corretto inserimento dei campi
'''
class LoginViewTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username="user",password="user")

    def test_login_view(self):
        response = self.client.post('/login/',{'username':'user','password':'user'})
        self.assertEqual(response.status_code,302)

    def test_login_view_wrong_password(self):
        response = self.client.post('/login/',{'username':'user','password':'wrong'})
        self.assertEqual(response.status_code,200)

    def test_login_view_wrong_username(self):
        response = self.client.post('/login/',{'username':'wrong','password':'user'})
        self.assertEqual(response.status_code,200)


'''
    Test Unitari per la view logout :
    - Test per il corretto reindirizzamento
'''
class LogoutViewTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username="user",password="user")

    def test_logout_view(self):
        self.client.login(username="user",password="user")
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code,302)


'''
    Test Unitari per la view home :
    - Test per la corretta visualizzazione della pagina
    - Test per vedere se utente è loggato
    - Test per vedere se utente è admin e reindirizzamento
'''
class HomeViewTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username="user",password="user")

    def test_home_view(self):
        self.client.login(username="user",password="user")
        response = self.client.get('/home/')
        self.assertEqual(response.status_code,200)

    def test_home_view_not_logged(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code,302)

    def test_home_view_admin_logged_redirect(self):
        User.objects.create_superuser(username="admin",password="admin")
        self.client.login(username="admin",password="admin")
        response = self.client.get('/home/')
        self.assertEqual(response.status_code,302)

    def test_home_view_list(self):
        self.client.login(username="user",password="user")
        response = self.client.get('/home/')
        self.assertEqual(list(response.context['lista_animali']),list(Animale.objects.all()))

    def test_home_view_template(self):
        self.client.login(username="user",password="user")
        response = self.client.get('/home/')
        self.assertTemplateUsed(response,'rifugioAnimali/home.html')

    '''
        Test Unitari per la view home admin :
        - Test per la corretta visualizzazione della pagina
        - Test per vedere se utente è loggato
        - Test per vedere se utente non admin e reindirizzamento
    '''
class HomeAdminTestCase(TestCase):
    def setUp(self):
        User.objects.create_superuser(username="admin",password="admin")

    def test_home_admin_view(self):
        self.client.login(username="admin",password="admin")
        response = self.client.get('/home_admin/')
        self.assertEqual(response.status_code,200)

    def test_home_admin_view_not_logged(self):
        response = self.client.get('/home_admin/')
        self.assertEqual(response.status_code,302)

    def test_home_admin_view_not_admin(self):
        User.objects.create_user(username="user",password="user")
        self.client.login(username="user",password="user")
        response = self.client.get('/home_admin/')
        self.assertEqual(response.status_code,302)

    def test_home_admin_view_template(self):
        self.client.login(username="admin",password="admin")
        response = self.client.get('/home_admin/')
        self.assertTemplateUsed(response,'rifugioAnimali/home_amministratore.html')

    def test_home_admin_view_list(self):
        self.client.login(username="admin",password="admin")
        response = self.client.get('/home_admin/')
        self.assertEqual(list(response.context['lista_moduli']),list(ModuloAdozione.objects.all()))

        

'''
    Test Unitari per la view moduloAdozione:
    - Test per la corretta visualizzazione della pagina
    - Test per vedere se utente è loggato
    - Test per vedere se è stato inviato un animale valido
'''    
class ModuloAdozioneViewTestCase(TestCase):
    def setUp(self):
        User.objects.create_superuser(username="admin",password="admin")
        Animale.objects.create(id=100,specie="cane",razza="labrador",descrizione="cane di taglia media",stato = "non_adottato")
        Animale.objects.create(id=101,specie="gatto",razza="persiano",descrizione="gatto di taglia media",stato = "adottato")
        Animale.objects.create(id=102,specie="cane",razza="pastore",descrizione="cane di taglia grande",stato = "in_attesa")

    def test_modulo_adozione_view(self):
        self.client.login(username="admin",password="admin")
        response = self.client.get('/modulo_adozione/100/')
        self.assertEqual(response.status_code,200)

    def test_modulo_adozione_view_not_logged(self):
        response = self.client.get('/modulo_adozione/100/')
        self.assertEqual(response.status_code,302)

    def test_modulo_adozione_view_animale_adottato(self):
        self.client.login(username="admin",password="admin")
        response = self.client.get('/modulo_adozione/101/')
        self.assertEqual(response.status_code,200)

    def test_modulo_adozione_view_animale_in_attesa(self):
        self.client.login(username="admin",password="admin")
        response = self.client.get('/modulo_adozione/102/')
        self.assertEqual(response.status_code,200)

    def test_modulo_adozione_view_animale_non_esistente(self):
        self.client.login(username="admin",password="admin")
        response = self.client.get('/modulo_adozione/103/')
        self.assertEqual(response.status_code,404)

    def test_modulo_adozione_view_template(self):
        self.client.login(username="admin",password="admin")
        response = self.client.get('/modulo_adozione/100/')
        self.assertTemplateUsed(response,'rifugioAnimali/modulo_adozione.html')


'''
    Test Unitari per la view gestioneAnimali:
    - Test per la corretta visualizzazione della pagina
    - Test per vedere se utente è loggato
    - Test per vedere se utente non admin e reindirizzamento
    - Test per vedere se la lista degli animali è corretta
'''
class GestioneAnimaliViewTestCase(TestCase):
    def setUp(self):
        User.objects.create_superuser(username="admin",password="admin")
        Animale.objects.create(id=100,specie="cane",razza="labrador",descrizione="cane di taglia media",stato = "non_adottato")
        Animale.objects.create(id=101,specie="gatto",razza="persiano",descrizione="gatto di taglia media",stato = "adottato")
        Animale.objects.create(id=102,specie="cane",razza="pastore",descrizione="cane di taglia grande",stato = "in_attesa") 

    def test_gestione_animali_view(self):
        self.client.login(username="admin",password="admin")
        response = self.client.get('/gestione_animali/')
        self.assertEqual(response.status_code,200)

    def test_gestione_animali_view_not_logged(self):
        response = self.client.get('/gestione_animali/')
        self.assertEqual(response.status_code,302)

    def test_gestione_animali_view_not_admin(self):
        User.objects.create_user(username="user",password="user")
        self.client.login(username="user",password="user")
        response = self.client.get('/gestione_animali/')
        self.assertEqual(response.status_code,302)

    def test_gestione_animali_view_template(self):
        self.client.login(username="admin",password="admin")
        response = self.client.get('/gestione_animali/')
        self.assertTemplateUsed(response,'rifugioAnimali/gestione_animali.html')

    def test_gestione_animali_view_list(self):
        self.client.login(username="admin",password="admin")
        response = self.client.get('/gestione_animali/')
        self.assertEqual(list(response.context['lista_animali']),list(Animale.objects.order_by("specie")))

'''
    Test Unitari per la view aggiungi_animale:
    - Test per la corretta visualizzazione della pagina
    - Test per vedere se utente è loggato
    - Test per vedere se utente non admin e reindirizzamento
'''

class AggiungiAnimaleViewTestCase(TestCase):
    def setUp(self):
        User.objects.create_superuser(username="admin",password="admin")
    
    def test_aggiungi_animale_view(self):
        self.client.login(username="admin",password="admin")
        response = self.client.get('/aggiungi_animale/')
        self.assertEqual(response.status_code,200)

    def test_aggiungi_animale_view_not_logged(self):
        response = self.client.get('/gestione_animali/')
        self.assertEqual(response.status_code,302)

    def test_aggiungi_animale_view_not_admin(self):
        User.objects.create_user(username="user",password="user")
        self.client.login(username="user",password="user")
        response = self.client.get('/aggiungi_animale/')
        self.assertEqual(response.status_code,302)

    def test_aggiungi_animale_view_template(self):
        self.client.login(username="admin",password="admin")
        response = self.client.get('/aggiungi_animale/')
        self.assertTemplateUsed(response,'rifugioAnimali/aggiungi_animale.html')

'''
    Test Unitari per la view invio_modulo_adozione:
    - Test per la corretta visualizzazione della pagina
    - Test per vedere se utente è loggato
    - Test per controllo se animale è esistente
    - Test per controllo se animale è disponibile
'''

class InvioModuloAdozioneViewTestCase(TestCase):
    def setUp(self):
        User.objects.create_superuser(username="admin",password="admin")
        User.objects.create_user(username="user",password="user")
        Animale.objects.create(id=100,specie="cane",razza="labrador",descrizione="cane di taglia media",stato = "non_adottato")
        
    def test_invio_modulo_adozione_view(self):
        self.client.login(username="user",password="user")
        response = self.client.post(
            reverse('invio_modulo_adozione', args=[100]), {
            'nomeCognome': 'Mario Rossi',
            'indirizzo': 'Via delle Rose 123',
            'recapito': '1234567890',
        })
        self.assertEqual(response.status_code,302)
        self.assertEqual(response.url, reverse('home'))

    def test_invio_modulo_adozione_view_not_logged(self):
        response = self.client.post(
            reverse('invio_modulo_adozione', args=[100]), {
            'nomeCognome': 'Mario Rossi',
            'indirizzo': 'Via delle Rose 123',
            'recapito': '1234567890',
        })
        self.assertEqual(response.status_code,302)

    def test_invio_modulo_adozione_view_animale_doesnt_exist(self):
        self.client.login(username="user",password="user")
        response = self.client.post(
            reverse('invio_modulo_adozione', args=[101]), {
            'nomeCognome': 'Mario Rossi',
            'indirizzo': 'Via delle Rose 123',
            'recapito': '1234567890',
        })
        with self.assertRaises(Animale.DoesNotExist):
            Animale.objects.get(id=101)

    def test_invio_modulo_adozione_view_nomeCognome_empty_field(self):
        self.client.login(username="user",password="user")
        response = self.client.post(
            reverse('invio_modulo_adozione', args=[100]), {
            'nomeCognome': '',
            'indirizzo': 'Via delle Rose 123',
            'recapito': '1234567890',
        })
        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(response, 'rifugioAnimali/modulo_adozione.html')
        self.assertContains(response, 'Non hai compilato tutti i campi')

    def test_invio_modulo_adozione_view_indirizzo_empty_field(self):
        self.client.login(username="user",password="user")
        response = self.client.post(
            reverse('invio_modulo_adozione', args=[100]), {
            'nomeCognome': 'Mario Rossi',
            'indirizzo': '',
            'recapito': '1234567890',
        })
        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(response, 'rifugioAnimali/modulo_adozione.html')
        self.assertContains(response, 'Non hai compilato tutti i campi')

    def test_invio_modulo_adozione_view_recapito_empty_field(self):
        self.client.login(username="user",password="user")
        response = self.client.post(
            reverse('invio_modulo_adozione', args=[100]), {
            'nomeCognome': 'Mario Rossi',
            'indirizzo': 'Via delle Rose 123',
            'recapito': '',
        })
        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(response, 'rifugioAnimali/modulo_adozione.html')
        self.assertContains(response, 'Non hai compilato tutti i campi')

    def test_invio_modulo_adozione_view_inserimento_corretto(self):
        self.client.login(username="user",password="user")
        response = self.client.post(
            reverse('invio_modulo_adozione', args=[100]), {
            'nomeCognome': 'Mario Rossi',
            'indirizzo': 'Via delle Rose 123',
            'recapito': '1234567890',
        })

        modulo = ModuloAdozione.objects.get(id=1)
        self.assertEqual(modulo.nomeCognome, 'Mario Rossi')
        self.assertEqual(modulo.indirizzo, 'Via delle Rose 123')
        self.assertEqual(modulo.recapito, '1234567890')

        animale = Animale.objects.get(id=100)
        self.assertEqual(animale.stato, 'IN_ATTESA')

        self.assertEqual(response.status_code,302)
        self.assertEqual(response.url, reverse('home'))

    def test_invio_modulo_adozione_view_animale_adottato(self):
        Animale.objects.create(id=101,specie="cane",razza="labrador",descrizione="cane di taglia media",stato = "ADOTTATO")
        self.client.login(username="user",password="user")
        response = self.client.post(
            reverse('invio_modulo_adozione', args=[101]), {
            'nomeCognome': 'Mario Rossi',
            'indirizzo': 'Via delle Rose 123',
            'recapito': '1234567890',
        })
        self.assertEqual(response.status_code,302)
        self.assertEqual(response.url, reverse('home'))

    def test_invio_modulo_adozione_view_animale_in_attesa(self):
        Animale.objects.create(id=101,specie="cane",razza="labrador",descrizione="cane di taglia media",stato = "IN_ATTESA")
        self.client.login(username="user",password="user")
        response = self.client.post(
            reverse('invio_modulo_adozione', args=[101]), {
            'nomeCognome': 'Mario Rossi',
            'indirizzo': 'Via delle Rose 123',
            'recapito': '1234567890',
        })

        self.assertEqual(response.status_code,302)
        self.assertEqual(response.url, reverse('home'))
