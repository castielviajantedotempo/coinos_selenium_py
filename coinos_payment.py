import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from pathlib import Path
import os

def test():
	print("teste")
	print("primeiro pagamento")
	make_payment("abysmalwinter85@walletofsatoshi.com","9")
	print("segundo pagamento")
	make_payment("abysmalwinter85@walletofsatoshi.com","9")

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

def make_payment(ln_address,value):
    servico=Service(ChromeDriverManager().install())

    options = webdriver.ChromeOptions()
    #options.add_argument("--headless=new")
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument('--disable-crash-reporter')

    navegador=webdriver.Chrome(service=servico, options=options)
    wait = WebDriverWait(navegador, 10) # waits for a maximum of 10 seconds

    navegador.get("http://coinos.io/login/")
    
    castiel_login = os.environ['USER_LOGIN']
    castiel_pass = os.environ['USER_PASS']
	
	#Login Page
    for x in range(10):
        if check_exists_by_xpath(navegador, '//input[@name="username"]'):
            navegador.find_element(By.XPATH, '//input[@name="username"]').send_keys(castiel_login)
            navegador.find_element(By.XPATH, '//input[@type="password"]').send_keys(castiel_pass)
            navegador.find_element(By.XPATH, '//button[@type="submit"]').click()
            break
        time.sleep(1)
    
    # make the payment
    # clicar no botão enviar
    element = "//button/div[text()='Enviar']"
    for x in range(10):
        if check_exists_by_xpath(navegador, element):
            submit = wait.until(EC.element_to_be_clickable((By.XPATH, element)))
            submit.click()
            break
        time.sleep(1)

    # passar o endereço lightning ('abysmalwinter85@walletofsatoshi.com')
    element = "//textarea[@name='text']"
    for x in range(10):
        if check_exists_by_xpath(navegador, element):
            navegador.find_element(By.XPATH, element).send_keys(ln_address)
            break
        time.sleep(1)

    # clicar em continuar
    element = "//button/div[text()='Continuar']"
    for x in range(10):
        if check_exists_by_xpath(navegador, element):
            continue_ = wait.until(EC.element_to_be_clickable((By.XPATH, element)))
            continue_.click()
            break
        time.sleep(1)

    # selecionar o valor em satoshis
    element = "//button[contains(@aria-label, 'Swap')]"
    for x in range(10):
        if check_exists_by_xpath(navegador, element):
            navegador.find_element(By.XPATH, element).click()
            break
        time.sleep(1)

    # scrola até o final da página
    navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # informa o valor
    string_value = str(value)
    for char in string_value:
        element = "//button[text()='"+char+"']"
        for x in range(10):
            if check_exists_by_xpath(navegador, element):
                navegador.find_element(By.XPATH, element).click()
                break
            time.sleep(1)

    # enviar o valor
    element = "//button[text()='Enviar']"
    for x in range(10):
        if check_exists_by_xpath(navegador, element):
            submit = wait.until(EC.element_to_be_clickable((By.XPATH, element)))
            submit.click()
            break
        time.sleep(1)

    # clicar de novo em enviar o valor
    element = "//button[text()='Enviar']"
    for x in range(10):
        if check_exists_by_xpath(navegador, element):
            submit = wait.until(EC.element_to_be_clickable((By.XPATH, element)))
            submit.click()
            break
        time.sleep(1)

    # checar se deu sucesso
    element = "//div[text()='Toque em qualquer lugar para continuar']"
    for x in range(10):
        if check_exists_by_xpath(navegador, element):
            print("Payment Success!")
            break
        time.sleep(1)
    
    #Closing Browser
    time.sleep(10)
    navegador.quit()

if __name__ == '__main__':
    test()
