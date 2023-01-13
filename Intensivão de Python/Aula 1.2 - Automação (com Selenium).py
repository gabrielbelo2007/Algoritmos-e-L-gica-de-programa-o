from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

navegador = webdriver.Chrome()

navegador.get(r"https://drive.google.com/drive/folders/14oLE59U1RqyRqlBbKpsyymW-mitvbtoh")
time.sleep(3)
button = navegador.find_element('xpath', '//*[@id=":1"]/div/c-wiz/div[2]/c-wiz/div[1]/c-wiz/div/c-wiz/div[1]/c-wiz/c-wiz/div/c-wiz/div/div/div/div[1]/div[2]')
button.click()
time.sleep(3)

tabela = pd.read_excel(r"C:\Users\Gabriel Belo\Downloads\Vendas - Dez.xlsx")
faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()
print(faturamento)
print(quantidade)
time.sleep(3)

navegador.get(r"https://www.google.com/intl/pt/gmail/about/")
time.sleep(3)
button1 = navegador.find_element('xpath', '/html/body/header/div/div/div/a[2]')
button1.click()
time.sleep(3)
navegador.find_element('xpath', '//*[@id="identifierId"]').send_keys("contadolol2007@gmail.com")
navegador.find_element('xpath', '//*[@id="identifierId"]').send_keys(Keys.ENTER)
time.sleep(3)
navegador.find_element('xpath', '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(r"g@B070410")
navegador.find_element('xpath', '//*[@id="identifierId"]').send_keys(Keys.ENTER)
time.sleep(5)

