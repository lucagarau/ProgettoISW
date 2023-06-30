from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from django.core.exceptions import ValidationError
import time

def testLoginAdmin():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/login/")

    loginBox = driver.find_element("id","acc_nomeUtente")
    loginBox.send_keys("paolo")

    passwordBox = driver.find_element("id","psw")
    passwordBox.send_keys("paolobosisio")

    passwordBox.send_keys(Keys.ENTER)
    time.sleep(5)

def testLoginUser():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/login/")

    loginBox = driver.find_element("id","acc_nomeUtente")
    loginBox.send_keys("alepani")

    passwordBox = driver.find_element("id","psw")
    passwordBox.send_keys("Ciaociao1!")

    passwordBox.send_keys(Keys.ENTER)
    time.sleep(5)

def testRegistrazioneUtente():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/registrazione/")

    nomeBox = driver.find_element("id","id_first_name")
    nomeBox.send_keys("Mario")

    cognomeBox = driver.find_element("id","id_last_name")
    cognomeBox.send_keys("Rossi")

    usernameBox = driver.find_element("id","id_username")
    usernameBox.send_keys("superMario")

    emailBox = driver.find_element("id","id_email")
    emailBox.send_keys("super@mario.nt")

    passwordBox = driver.find_element("id","id_password1")
    passwordBox.send_keys("Ciaociao1!")

    passwordBox = driver.find_element("id","id_password2")
    passwordBox.send_keys("Ciaociao1!")

    passwordBox.send_keys(Keys.ENTER)
    #registrazione effettuata

    time.sleep(5)
    #login con nuove credenziali
    driver.get("http://localhost:8000/login/")
    loginBox = driver.find_element("id","acc_nomeUtente")
    loginBox.send_keys("superMario")

    passwordBox = driver.find_element("id","psw")
    passwordBox.send_keys("Ciaociao1!")

    passwordBox.send_keys(Keys.ENTER)
    time.sleep(5)
    

def testRegistrazioneUtenteErrore():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/registrazione/")

    nomeBox = driver.find_element("id","id_first_name")
    nomeBox.send_keys("Mario")

    cognomeBox = driver.find_element("id","id_last_name")
    cognomeBox.send_keys("")

    usernameBox = driver.find_element("id","id_username")
    usernameBox.send_keys("superMario")

    emailBox = driver.find_element("id","id_email")
    emailBox.send_keys("super@mario.nt")

    passwordBox = driver.find_element("id","id_password1")
    passwordBox.send_keys("Ciaociao1!")

    passwordBox = driver.find_element("id","id_password2")
    passwordBox.send_keys("Ciaociao1!")

    passwordBox.send_keys(Keys.ENTER)
    time.sleep(5)

def testVisualizzazioneAnimaleAdozione():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/")

    #login
    loginBox = driver.find_element("id","acc_nomeUtente")
    loginBox.send_keys("superMario")

    passwordBox = driver.find_element("id","psw")
    passwordBox.send_keys("Ciaociao1!")

    passwordBox.send_keys(Keys.ENTER)
    time.sleep(5)

    #premiAdotta
    driver.find_element(By.PARTIAL_LINK_TEXT,"Adotta").click()
    time.sleep(5)

def testRichiestaAdozioneAnimale():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/")

    #login
    loginBox = driver.find_element("id","acc_nomeUtente")
    loginBox.send_keys("superMario")

    passwordBox = driver.find_element("id","psw")
    passwordBox.send_keys("Ciaociao1!")

    passwordBox.send_keys(Keys.ENTER)
    time.sleep(5)

    #premiAdotta
    driver.find_element(By.PARTIAL_LINK_TEXT,"Adotta").click()
    time.sleep(5)
    #compilazione modulo adozione
    nomeBox = driver.find_element("id","adotta_nome")
    nomeBox.send_keys("Mario")

    indirizzoBox = driver.find_element("id","adotta_indirizzo")
    indirizzoBox.send_keys("via da qui 45")

    recapitoBox = driver.find_element("id","adotta_recapito")
    recapitoBox.send_keys("1234567890")

    time.sleep(3)

    adotta = driver.find_element("id","adotta")
    adotta.send_keys(Keys.ENTER)

    time.sleep(5)

def testRichiestaAdozioneAnimaleCampoVuoto():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/")

    #login
    loginBox = driver.find_element("id","acc_nomeUtente")
    loginBox.send_keys("superMario")

    passwordBox = driver.find_element("id","psw")
    passwordBox.send_keys("Ciaociao1!")

    passwordBox.send_keys(Keys.ENTER)
    time.sleep(5)

    #premiAdotta
    driver.find_element(By.PARTIAL_LINK_TEXT,"Adotta").click()
    time.sleep(5)
    #compilazione modulo adozione
    nomeBox = driver.find_element("id","adotta_nome")
    nomeBox.send_keys("Mario")

    indirizzoBox = driver.find_element("id","adotta_indirizzo")
    indirizzoBox.send_keys("")

    recapitoBox = driver.find_element("id","adotta_recapito")
    recapitoBox.send_keys("1234567890")

    time.sleep(3)

    adotta = driver.find_element("id","adotta")
    adotta.send_keys(Keys.ENTER)

    time.sleep(5)

def testGestioneRichiestaAccetta():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/")

    #login admin
    loginBox = driver.find_element("id","acc_nomeUtente")
    loginBox.send_keys("alestaff")

    passwordBox = driver.find_element("id","psw")
    passwordBox.send_keys("Ciaociao1!")

    time.sleep(3)

    passwordBox.send_keys(Keys.ENTER)

    time.sleep(3)

    #home admin
    accettaBox = driver.find_element("id","acc_19")
    accettaBox.send_keys(Keys.ENTER)

    time.sleep(5)

def testGestioneRichiestaRifiuta():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/")

    #login admin
    loginBox = driver.find_element("id","acc_nomeUtente")
    loginBox.send_keys("alestaff")

    passwordBox = driver.find_element("id","psw")
    passwordBox.send_keys("Ciaociao1!")

    time.sleep(3)

    passwordBox.send_keys(Keys.ENTER)

    time.sleep(3)

    #home admin
    accettaBox = driver.find_element("id","rif_18")
    accettaBox.send_keys(Keys.ENTER)

    time.sleep(5)

def testVisualizzaGestioneAnimali():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/login")

    #login admin
    loginBox = driver.find_element("id","acc_nomeUtente")
    loginBox.send_keys("alestaff")

    passwordBox = driver.find_element("id","psw")
    passwordBox.send_keys("Ciaociao1!")

    time.sleep(3)

    passwordBox.send_keys(Keys.ENTER)

    time.sleep(3)

    #home admin
    driver.find_element("id","gestione_animali").click()
    time.sleep(5)

def testModificaAnimale():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/login")

    #login admin
    loginBox = driver.find_element("id","acc_nomeUtente")
    loginBox.send_keys("alestaff")

    passwordBox = driver.find_element("id","psw")
    passwordBox.send_keys("Ciaociao1!")

    time.sleep(3)

    passwordBox.send_keys(Keys.ENTER)

    time.sleep(3)

    #home admin
    driver.find_element("id","gestione_animali").click()
    time.sleep(5)

    driver.find_element("id","mod_8").click()
    time.sleep(3)

    razzaBox = driver.find_element("id","razza")
    razzaBox.clear()
    razzaBox.send_keys("pelosetto")

    time.sleep(3)

    driver.find_element("id","modifica").click()

    time.sleep(5)

def testModificaAnimaleErrore():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/login")

    #login admin
    loginBox = driver.find_element("id","acc_nomeUtente")
    loginBox.send_keys("alestaff")

    passwordBox = driver.find_element("id","psw")
    passwordBox.send_keys("Ciaociao1!")

    time.sleep(3)

    passwordBox.send_keys(Keys.ENTER)

    time.sleep(3)

    #home admin
    driver.find_element("id","gestione_animali").click()
    time.sleep(5)

    driver.find_element("id","mod_8").click()
    time.sleep(3)

    razzaBox = driver.find_element("id","razza")
    razzaBox.clear()
    razzaBox.send_keys("")

    time.sleep(3)

    driver.find_element("id","modifica").click()

    time.sleep(5)

def testEliminaAnimale():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/login")

    #login admin
    loginBox = driver.find_element("id","acc_nomeUtente")
    loginBox.send_keys("alestaff")

    passwordBox = driver.find_element("id","psw")
    passwordBox.send_keys("Ciaociao1!")

    time.sleep(3)

    passwordBox.send_keys(Keys.ENTER)

    time.sleep(3)

    #home admin
    driver.find_element("id","gestione_animali").click()
    time.sleep(3)

    #elimina animale
    driver.find_element("id","elim_1").click()
    time.sleep(5)

def testAggiungiAnimale():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/login")

    #login admin
    loginBox = driver.find_element("id","acc_nomeUtente")
    loginBox.send_keys("alestaff")

    passwordBox = driver.find_element("id","psw")
    passwordBox.send_keys("Ciaociao1!")

    time.sleep(3)

    passwordBox.send_keys(Keys.ENTER)

    time.sleep(3)

    #home admin
    driver.find_element("id","gestione_animali").click()
    time.sleep(3)

    driver.find_element("id","aggiungi").click()
    time.sleep(3)

    specieBox = driver.find_element("id","specie")
    specieBox.send_keys("cane")

    razzaBox = driver.find_element("id","razza")
    razzaBox.send_keys("barboncino")

    etaBox = driver.find_element("id","eta")
    etaBox.send_keys("12")

    descrizioneBox = driver.find_element("id","descrizione")
    descrizioneBox.send_keys("cane molto violento")

    time.sleep(3)
    driver.find_element("id","aggiungi").click()
    time.sleep(5)

def testAggiungiAnimaleErrore():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/login")

    #login admin
    loginBox = driver.find_element("id","acc_nomeUtente")
    loginBox.send_keys("alestaff")

    passwordBox = driver.find_element("id","psw")
    passwordBox.send_keys("Ciaociao1!")

    time.sleep(3)

    passwordBox.send_keys(Keys.ENTER)

    time.sleep(3)

    #home admin
    driver.find_element("id","gestione_animali").click()
    time.sleep(3)

    driver.find_element("id","aggiungi").click()
    time.sleep(3)

    specieBox = driver.find_element("id","specie")
    specieBox.send_keys("")

    razzaBox = driver.find_element("id","razza")
    razzaBox.send_keys("barboncino")

    etaBox = driver.find_element("id","eta")
    etaBox.send_keys("12")

    descrizioneBox = driver.find_element("id","descrizione")
    descrizioneBox.send_keys("cane molto violento")

    time.sleep(3)
    driver.find_element("id","aggiungi").click()
    time.sleep(5)

def testLogout():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/login/")

    loginBox = driver.find_element("id","acc_nomeUtente")
    loginBox.send_keys("alepani")

    passwordBox = driver.find_element("id","psw")
    passwordBox.send_keys("Ciaociao1!")

    passwordBox.send_keys(Keys.ENTER)
    time.sleep(3)

    driver.find_element("id","Logout").click()
    time.sleep(5)



if __name__ == "__main__":
    #testLoginAdmin()
    #testLoginUser()
    #testRegistrazioneUtenteErrore()
    #testRegistrazioneUtente()
    #testVisualizzazioneAnimaleAdozione()
    #testRichiestaAdozioneAnimale()
    #testRichiestaAdozioneAnimaleCampoVuoto()
    #testGestioneRichiestaAccetta()
    #testGestioneRichiestaRifiuta()
    #testVisualizzaGestioneAnimali()
    #testModificaAnimale()
    #testModificaAnimaleErrore()
    #testEliminaAnimale()
    #testAggiungiAnimale()
    #testAggiungiAnimaleErrore()
    testLogout()
