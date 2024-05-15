from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from bs4 import BeautifulSoup 
import time


options = webdriver.ChromeOptions()
options.add_argument('--headless') 
edge_driver = '\Users\mcdni\OneDrive\Área de Trabalho\Browserless\venv\drivers'
driver = webdriver.Edge(options=options)


url = "https://ww1.receita.fazenda.df.gov.br/icms/sintegra-consulta"

try:
    
    driver.get(url)

    
    wait = WebDriverWait(driver, 10)
    cnpj_field = wait.until(EC.presence_of_element_located((By.ID, "cnpj")))

    cnpj_field.send_keys("54608244000180")

    consulta_button = driver.find_element(By.ID, "bt_consulta")
    consulta_button.click()

    time.sleep(5)

    page_source = driver.page_source

    soup = BeautifulSoup(page_source, 'html.parser')

    resultado = soup.find('div', id='resultado')
    if resultado:
        print(resultado.text)
    else:
        print("Nenhum resultado encontrado")

finally:
    driver.quit()