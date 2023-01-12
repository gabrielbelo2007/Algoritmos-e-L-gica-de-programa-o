# Lembrar de sempre importar as bibliotecas usadas no código
import pandas as pd
import pyautogui as pa
import time
import pyperclip

# Código para gravar a posição do mouse na tela
'''
time.sleep(5)
pyautogui.position()
'''

pa.PAUSE = 2  # Regular a velocidade

# Passo 1: Entrar no drive

pa.press('win')
pa.write('Opera')
pa.press('enter')
pa.write(r"https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pa.press('enter')

time.sleep(5)

# Passo 2: Baixar os dados

pa.click(x=391, y=284, clicks=2)
time.sleep(3)
pa.click(x=488, y=279)
pa.click(x=1719, y=194)
pa.click(x=1483, y=598)
time.sleep(4)

# Passo 3: Analisar os dados

tabela = pd.read_excel(r"C:\Users\Gabriel Belo\Downloads\Vendas - Dez.xlsx")
faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()
print(faturamento)
print(quantidade)
time.sleep(3)

# Passo 4: Enviar o email

pa.hotkey("ctrl", "t")
pa.write(r"https://mail.google.com/mail/u/0/#inbox")
pa.press("enter")

pa.click(x=147, y=212)
pa.write("contadolol2007@gmail.com")
pa.press("tab")

pa.press("tab")
pyperclip.copy("Relatório de vendas")
pa.hotkey("ctrl", "v")

pa.press("tab")
texto = f"""
Prezados,

Segue relatório de vendas.
Faturamento: R${faturamento:,.2f}
Quantidade de produtos vendidos: {quantidade:,}

Qualquer dúvida estou à disposição.
Att.,
Gabriel Belo
"""

pyperclip.copy(texto)
pa.hotkey("ctrl", "v")
pa.hotkey("ctrl", "enter")
