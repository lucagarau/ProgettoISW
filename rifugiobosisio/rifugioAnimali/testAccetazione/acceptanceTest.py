from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
    driver.find_element("id","Logout").click()
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

    driver.find_element("id","Logout").click()
    time.sleep(5)


if __name__ == "__main__":
    testLoginAdmin()
    testLoginUser()