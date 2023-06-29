from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import TestCase
from django.contrib.auth.models import User
import time

class AcceptanceTest(TestCase):
    databases = {'default', 'test'}

    def testLoginAdmin(self):
        User.objects.create_superuser(username="paolo", password="paolobosisio")
        driver = webdriver.Chrome()
        driver.get("http://localhost:8000/login/")

        loginBox = driver.find_element("id","acc_nomeUtente")
        loginBox.send_keys("paolo")

        passwordBox = driver.find_element("id","psw")
        passwordBox.send_keys("paolobosisio")

        passwordBox.send_keys(Keys.ENTER)
        time.sleep(5)
        driver.find_element("id","Logout").click()
        time.sleep(5)

    def testLoginUser(self):
        User.objects.create_user(username="alepani", password="Ciaociao1!")
        driver = webdriver.Chrome()
        driver.get("http://localhost:8000/login/")

        loginBox = driver.find_element("id","acc_nomeUtente")
        loginBox.send_keys("alepani")

        passwordBox = driver.find_element("id","psw")
        passwordBox.send_keys("Ciaociao1!")

        passwordBox.send_keys(Keys.ENTER)
        time.sleep(5)

        driver.find_element("id","Logout").click()
        time.sleep(5)


