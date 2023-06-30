from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from django.core.exceptions import ValidationError
import time
from django.contrib.auth.models import User
from django.test import TestCase

class TestLogin(TestCase):
    databases = {'default'}

    def testLoginAdmin(self):
        driver = webdriver.Chrome()
        driver.get("http://localhost:8000/login/")

        utente = User.objects.create_superuser(username="admin",password="admin")
        utente.save()

        loginBox = driver.find_element("id","acc_nomeUtente")
        loginBox.send_keys("admin")

        passwordBox = driver.find_element("id","psw")
        passwordBox.send_keys("admin")

        passwordBox.send_keys(Keys.ENTER)
        time.sleep(5)
        driver.find_element("id","Logout").click()
        time.sleep(5)
        User.objects.get(username="admin").delete()


    def testLoginUser(self):
        User.objects.create_user(username="user",password="user")
        driver = webdriver.Chrome()
        driver.get("http://localhost:8000/login/")

        loginBox = driver.find_element("id","acc_nomeUtente")
        loginBox.send_keys("user")

        passwordBox = driver.find_element("id","psw")
        passwordBox.send_keys("user")
        passwordBox.send_keys(Keys.ENTER)
        time.sleep(5)

        driver.find_element("id","Logout").click()
        time.sleep(5)
        User.objects.get(username = "user").delete()