from selenium import webdriver  # Selecionando apenas um "livro" da biblioteca do selenium
from selenium.webdriver.common.keys import Keys

# para rodar o chrome em 2º plano
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.headless = True
# navegador = webdriver.Chrome(options=chrome_options)

# Passo 1: Abrir o chrome e a aba do google

navegador = webdriver.Chrome()
navegador.get("https://www.google.com/")


# Passo 2: Pegar a cotação do dólar, euro e ouro

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dólar")
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cota_dol = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")


navegador.get("https://www.google.com/")
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cota_eur = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")


navegador.get("https://www.melhorcambio.com/ouro-hoje")
cota_our = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
cota_our = cota_our.replace(",", ".")


# Passo 3: Importar a lista de produtos
import pandas as pd

tabela = pd.read_excel(r"C:\Users\Gabriel Belo\Downloads\Aula 3\Produtos.xlsx")


# Passo 4: Recalcular o preço dos produtos (partindo das novas cotações)

# Localizando os valores de cotações passados e atualizando pelos novos
tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cota_dol)
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cota_eur)
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cota_our)

# Atualizar os valores do preço base (preço (base) antigo * nova cotação)

tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]

# Atualizar os valores do preço de venda (novo preço de base * margem de lucro)

tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]


# Passo 5: Exportar em uma nova base de dados

# index=False é para não exportar os índices da tabela
tabela.to_excel(r"C:\Users\Gabriel Belo\Downloads\Produtos Novo.xlsx", index=False)
