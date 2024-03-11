
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from time import sleep

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('start-maximized')
chromeOptions.add_argument('--headless')
driver = webdriver.Chrome(options=chromeOptions)
# driver = webdriver.Chrome() 

driver.get('https://www.google.com')
time.sleep(1)

# COTAÇÃO DO DOLAR
driver.find_element(By.XPATH, '//*[@id="APjFqb"]').send_keys('Cotação do Dólar') 
time.sleep(1)

# driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()
driver.find_element(By.XPATH, '//*[@id="APjFqb"]').send_keys(Keys.ENTER)
time.sleep(1)

dolar = driver.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
print('Cotação do Dólar: ', dolar)
time.sleep(1)


# COTAÇÃO DO EURO
driver.find_element(By.XPATH, '//*[@id="APjFqb"]').clear()
time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="APjFqb"]').send_keys('Cotação do Euro') 
time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="APjFqb"]').send_keys(Keys.ENTER)
time.sleep(1)

euro = driver.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text 
print('Cotação do Euro: ', euro)
time.sleep(1)

# COTAÇÃO DO PESO ARGENTINO
driver.find_element(By.XPATH, '//*[@id="APjFqb"]').clear()
time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="APjFqb"]').send_keys('Cotação do Peso Argentino') 
time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="APjFqb"]').send_keys(Keys.ENTER)
time.sleep(1)

peso_argentino = driver.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text 
print('Cotação do Peso Argentino: ', peso_argentino)
time.sleep(1)

driver.close()
driver.quit()

# data e hora atual
from datetime import datetime
agora = datetime.now()

data = agora.strftime('%d/%m/%Y')
hora = agora.strftime('%H:%M')

print(data, hora)

# SALVAR DADOS EM ARQUIVO csv
# cria um dateframe com colunas vazias
# df = pd.DataFrame(columns=['Data', 'Hora', 'Dolar', 'Euro', 'Peso Argentino'])
# print(df)

#cria um arquivo csv se não existir
# df.to_csv('cotacoes.csv', index=False)

# ler arquivo csv
df = pd.read_csv('cotacoes.csv')

#adiciona uma linha ao dataframe
df.loc[len(df)] = [data, hora, dolar, euro, peso_argentino]

df.to_csv('cotacoes.csv', index=False)
print(df)