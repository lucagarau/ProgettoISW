from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from .models import *
from django.test import LiveServerTestCase
from django.contrib.auth.models import User
import time        

'''
    Test di accettazione per la pagina di login e logout
    - test_login_user: testa il login di un utente
    - test_login_admin: testa il login di un admin
    - test_logout: testa il logout di un utente
'''

class TestAccetazioneLogin(LiveServerTestCase):
    def setUp(self):
        super().setUp()
        self.driver = webdriver.Chrome()
        self.animale = Animale.objects.create(id=101,specie="gatto",razza="siamese",eta=12,descrizione="gatto molto violento",stato = "NON_ADOTTATO")
        User.objects.create_user(username="user",password="Ciaociao1!")
        User.objects.create_superuser(username="admin",password="admin")
        ModuloAdozione.objects.create(id=102, nomeCognome='nome cognome', recapito='3333333333', indirizzo='via roma', animale=self.animale)


    def test_login_user(self):
        self.driver.get(self.live_server_url + "/login/")

        time.sleep(2)

        loginBox = self.driver.find_element("id","acc_nomeUtente")
        loginBox.send_keys("user")

        passwordBox = self.driver.find_element("id","psw")
        passwordBox.send_keys("Ciaociao1!")

        passwordBox.send_keys(Keys.ENTER)
        time.sleep(5)

    def test_login_admin(self):
        self.driver.get(self.live_server_url + "/login/")
        loginBox = self.driver.find_element("id","acc_nomeUtente")
        loginBox.send_keys("admin")
        passwordBox = self.driver.find_element("id","psw")
        passwordBox.send_keys("admin")
        passwordBox.send_keys(Keys.ENTER)
        time.sleep(5)

    def test_logout(self):
        self.client.login(username='admin', password='admin')
        self.driver.get(self.live_server_url + "/login/")
        loginBox = self.driver.find_element("id","acc_nomeUtente")
        loginBox.send_keys("admin")
        passwordBox = self.driver.find_element("id","psw")
        passwordBox.send_keys("admin")
        passwordBox.send_keys(Keys.ENTER)
        time.sleep(2)
        self.driver.find_element("id","Logout").click()
        time.sleep(5)

'''
    Test di accettazione per la pagina di registrazione
    - test_registrazione_utente: testa la registrazione di un utente
    - test_registrazione_utente_errore: testa la registrazione di un utente con errori
'''
class TestAccetazioneRegistrazione(LiveServerTestCase):
    def setUp(self):
        super().setUp()
        self.driver = webdriver.Chrome()
        self.animale = Animale.objects.create(id=101,specie="gatto",razza="siamese",eta=12,descrizione="gatto molto violento",stato = "NON_ADOTTATO")

    def test_registrazione_utente(self):
        self.driver.get(self.live_server_url + "/registrazione/")

        nomeBox = self.driver.find_element("id","id_first_name")
        nomeBox.send_keys("Mario")

        cognomeBox = self.driver.find_element("id","id_last_name")
        cognomeBox.send_keys("Rossi")

        usernameBox = self.driver.find_element("id","id_username")
        usernameBox.send_keys("superMario")

        emailBox = self.driver.find_element("id","id_email")
        emailBox.send_keys("super@mario.nt")

        passwordBox = self.driver.find_element("id","id_password1")
        passwordBox.send_keys("Ciaociao1!")

        passwordBox = self.driver.find_element("id","id_password2")
        passwordBox.send_keys("Ciaociao1!")
        time.sleep(5)

        passwordBox.send_keys(Keys.ENTER)
        #registrazione effettuata

        time.sleep(2)
        #login con nuove credenziali
        self.driver.get(self.live_server_url + "/login/")
        loginBox = self.driver.find_element("id","acc_nomeUtente")
        loginBox.send_keys("superMario")

        passwordBox = self.driver.find_element("id","psw")
        passwordBox.send_keys("Ciaociao1!")

        passwordBox.send_keys(Keys.ENTER)
        time.sleep(2)
    

    def test_registrazione_utente_errore(self):
        self.driver.get(self.live_server_url + "/registrazione/")

        nomeBox = self.driver.find_element("id","id_first_name")
        nomeBox.send_keys("Mario")

        cognomeBox = self.driver.find_element("id","id_last_name")
        cognomeBox.send_keys("")

        usernameBox = self.driver.find_element("id","id_username")
        usernameBox.send_keys("superMario")

        emailBox = self.driver.find_element("id","id_email")
        emailBox.send_keys("super@mario.nt")

        passwordBox = self.driver.find_element("id","id_password1")
        passwordBox.send_keys("Ciaociao1!")

        passwordBox = self.driver.find_element("id","id_password2")
        passwordBox.send_keys("Ciaociao1!")
        time.sleep(5)

        passwordBox.send_keys(Keys.ENTER)
        time.sleep(5)

'''
    Test di accettazione per la pagina di visualizzazione animali e richiesta adozione
    - test_visualizzazione_animale_adozione: testa la visualizzazione di un animale
    - test_richiesta_adozione_animale: testa la richiesta di adozione di un animale
    - test_richiesta_adozione_animale_campo_vuoto: testa la richiesta di adozione di un animale con campi vuoti
'''
class TestAccettazioneRichiestaAdozione(LiveServerTestCase):
    def setUp(self):
        super().setUp()
        self.driver = webdriver.Chrome()
        self.animale = Animale.objects.create(id=101,specie="gatto",razza="siamese",eta=12,descrizione="gatto molto violento",stato = "NON_ADOTTATO")
        self.utente = User.objects.create_user(username="user",password="Ciaociao1!")

    def test_visualizzazione_animale_adozione(self):
        login("user","Ciaociao1!",self.driver,self.live_server_url)
        time.sleep(5)
        #premiAdotta
        self.driver.find_element("id","adotta_101").click()
        time.sleep(2)

    def test_richiesta_adozione_animale(self):
        login("user","Ciaociao1!",self.driver,self.live_server_url)

        #premiAdotta
        self.driver.find_element("id","adotta_101").click()
        time.sleep(5)
        #compilazione modulo adozione
        nomeBox = self.driver.find_element("id","adotta_nome")
        nomeBox.send_keys("Mario")

        indirizzoBox = self.driver.find_element("id","adotta_indirizzo")
        indirizzoBox.send_keys("via da qui 45")

        recapitoBox = self.driver.find_element("id","adotta_recapito")
        recapitoBox.send_keys("1234567890")

        time.sleep(2)

        adotta = self.driver.find_element("id","adotta")
        adotta.send_keys(Keys.ENTER)

        time.sleep(2)

    def test_richiesta_adozione_animale_campo_vuoto(self):
        login("user","Ciaociao1!",self.driver,self.live_server_url)
        time.sleep(5)

        #premiAdotta
        self.driver.find_element("id","adotta_101").click()
        time.sleep(2)

        #compilazione modulo adozione
        nomeBox = self.driver.find_element("id","adotta_nome")
        nomeBox.send_keys("Mario")
        indirizzoBox = self.driver.find_element("id","adotta_indirizzo")
        indirizzoBox.send_keys("")
        recapitoBox = self.driver.find_element("id","adotta_recapito")
        recapitoBox.send_keys("1234567890")
        time.sleep(2)
        adotta = self.driver.find_element("id","adotta")
        adotta.send_keys(Keys.ENTER)
        time.sleep(2)


'''
    Test di accettazione per la pagina di visualizzazione animali e richiesta adozione
    - test_gestione_richiesta_accetta: testa la gestione di una richiesta di adozione accettata
    - test_gestione_richiesta_rifiuta: testa la gestione di una richiesta di adozione rifiutata
'''
class TestAccettazioneGestioneRichiesta(LiveServerTestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(username="admin",password="admin")
        self.animale = Animale.objects.create(id=101,specie="gatto",razza="siamese",eta=12,descrizione="gatto molto violento",stato = "IN_ATTESA")
        self.modulo = ModuloAdozione.objects.create(id=101,nomeCognome="Mario Mariottide",indirizzo="via da qui 45",recapito="1234567890",animale=self.animale)

        self.driver = webdriver.Chrome()

    def test_gestione_richiesta_accetta(self):
        login("admin","admin",self.driver,self.live_server_url)
        time.sleep(10)

        #visualizza gli animali in attesa
        self.driver.find_element("id","gestione_animali").click()
        time.sleep(5)
        self.driver.find_element("id","home").click()
        time.sleep(2)

        #home admin
        accettaBox = self.driver.find_element("id","acc_101")
        accettaBox.send_keys(Keys.ENTER)
        time.sleep(2)

        #visualizza se l'animale è stato adottato
        self.driver.find_element("id","gestione_animali").click()
        time.sleep(5)

    def test_gestione_richiesta_rifiuta(self):
        login("admin","admin",self.driver,self.live_server_url)
        time.sleep(10)
        #visualizza gli animali in attesa
        self.driver.find_element("id","gestione_animali").click()
        time.sleep(5)
        self.driver.find_element("id","home").click()
        time.sleep(2)

    
        #home admin
        accettaBox = self.driver.find_element("id","rif_101")
        accettaBox.send_keys(Keys.ENTER)
        self.driver.find_element("id","gestione_animali").click()
        time.sleep(5)

'''
    Test di accettazione per la pagina di gestione animali
    - test_visualizza_gestione_animali: testa la visualizzazione della pagina di gestione animali
    - test_modifica_animale: testa la modifica di un animale
    - test_elimina_animale: testa l'eliminazione di un animale
    - test_aggiungi_animale: testa l'aggiunta di un animale
        
'''
class TestAccettazioneGestioneAnimali(LiveServerTestCase):
    def setUp(self):
        User.objects.create_superuser(username="admin",password="admin")
        Animale.objects.create(id=101,specie="gatto",razza="siamese",eta=12,descrizione="gatto molto violento",stato = "NON_ADOTTATO")
        Animale.objects.create(id=102,specie="cane",razza="pastore tedesco",eta=12,descrizione="cane molto violento",stato = "ADOTTATO")
        self.driver = webdriver.Chrome()

    def test_visualizza_gestione_animali(self):
        login("admin","admin",self.driver,self.live_server_url)
        time.sleep(10)
        #home admin
        self.driver.find_element("id","gestione_animali").click()
        time.sleep(2)

    def test_modifica_animale(self):
        login("admin","admin",self.driver,self.live_server_url)
        time.sleep(10)

        #home admin
        self.driver.find_element("id","gestione_animali").click()
        time.sleep(5)

        self.driver.find_element("id","mod_101").click()
        time.sleep(3)

        razzaBox = self.driver.find_element("id","razza")
        razzaBox.clear()
        razzaBox.send_keys("pelosetto")

        time.sleep(3)

        self.driver.find_element("id","modifica").click()

        time.sleep(5)

    def test_modifica_animale_errore(self):
        login("admin","admin",self.driver,self.live_server_url)
        time.sleep(10)

        #home admin
        self.driver.find_element("id","gestione_animali").click()
        time.sleep(5)

        self.driver.find_element("id","mod_101").click()
        time.sleep(3)

        razzaBox = self.driver.find_element("id","razza")
        razzaBox.clear()
        razzaBox.send_keys("")

        time.sleep(3)

        self.driver.find_element("id","modifica").click()

        time.sleep(5)

    def test_elimina_animale(self):
        login("admin","admin",self.driver,self.live_server_url)
        time.sleep(10)

        #home admin
        self.driver.find_element("id","gestione_animali").click()
        time.sleep(3)

        #elimina animale
        self.driver.find_element("id","elim_102").click()
        time.sleep(5)

    def test_aggiungi_animale(self):
        login("admin","admin",self.driver,self.live_server_url)
        time.sleep(10)

        #home admin
        self.driver.find_element("id","gestione_animali").click()
        time.sleep(3)

        self.driver.find_element("id","aggiungi").click()
        time.sleep(3)

        specieBox = self.driver.find_element("id","specie")
        specieBox.send_keys("cane")

        razzaBox = self.driver.find_element("id","razza")
        razzaBox.send_keys("barboncino")

        etaBox = self.driver.find_element("id","eta")
        etaBox.send_keys("12")

        descrizioneBox = self.driver.find_element("id","descrizione")
        descrizioneBox.send_keys("cane molto violento")

        time.sleep(3)
        self.driver.find_element("id","aggiungi").click()
        time.sleep(5)

    def test_aggiungi_animale_errore(self):
        login("admin","admin",self.driver,self.live_server_url)
        time.sleep(10)

        #home admin
        self.driver.find_element("id","gestione_animali").click()
        time.sleep(3)

        self.driver.find_element("id","aggiungi").click()
        time.sleep(3)

        specieBox = self.driver.find_element("id","specie")
        specieBox.send_keys("")

        razzaBox = self.driver.find_element("id","razza")
        razzaBox.send_keys("barboncino")

        etaBox = self.driver.find_element("id","eta")
        etaBox.send_keys("12")

        descrizioneBox = self.driver.find_element("id","descrizione")
        descrizioneBox.send_keys("cane molto violento")

        time.sleep(3)
        self.driver.find_element("id","aggiungi").click()
        time.sleep(5)




def login(user, password, driver,link):
    driver.get(link + "/login/")
    usernameBox = driver.find_element("id","acc_nomeUtente")
    usernameBox.send_keys(user)
    passwordBox = driver.find_element("id","psw")
    passwordBox.send_keys(password)
    passwordBox.send_keys(Keys.ENTER)


