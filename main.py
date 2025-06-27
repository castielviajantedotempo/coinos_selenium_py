import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def check_exists_by_xpath(webdriver, xpath):
    try:
        webdriver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_id(webdriver,ID):
    try:
        webdriver.find_element(By.ID, ID)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_class(webdriver,Class):
    try:
        webdriver.find_element(By.CLASS_NAME, Class)
    except NoSuchElementException:
        return False
    return True


servico=Service(ChromeDriverManager().install())
navegador=webdriver.Chrome(service=servico)

navegador.get("http://coinos.io/login/")
navegador.maximize_window()

#navegador.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/p/a').click()

#Login Page
for x in range(10):
    if check_exists_by_xpath(navegador, '/html/body/div/main/main/div/form/input[3]'):
        navegador.find_element(By.XPATH, '/html/body/div/main/main/div/form/input[3]').send_keys('lula9dedos')
        navegador.find_element(By.XPATH, '/html/body/div/main/main/div/form/label/input').send_keys('PegaNoMeuBilau')
        navegador.find_element(By.XPATH, '/html/body/div/main/main/div/form/button[1]').click()
        break
    time.sleep(1)

#Get Wallet Value
for x in range(10):
    if check_exists_by_xpath(navegador, '/html/body/div/main/main/div/div[1]/div[3]/div/div[1]/div/div/div[1]/div/div/div/h2/div'):
        value = navegador.find_element(By.XPATH, '/html/body/div/main/main/div/div[1]/div[3]/div/div[1]/div/div/div[1]/div/div/div/h2/div').text
        print(value)
        break
    time.sleep(1)

#Payments Page
for x in range(10):
    if(check_exists_by_xpath(navegador, '/html/body/div/main/main/header/nav/a[3]/button')):
        navegador.find_element(By.XPATH, '/html/body/div/main/main/header/nav/a[3]/button').click()
        break
    time.sleep(1)

for x in range(10):
    if(check_exists_by_xpath(navegador, '/html/body/div/main/main/div/div[1]/div[1]/a[3]')):
        navegador.find_element(By.XPATH, '/html/body/div/main/main/div/div[1]/div[1]/a[3]').click()
        break
    time.sleep(1)

#Closing Browser
time.sleep(10)
navegador.quit()
                      

