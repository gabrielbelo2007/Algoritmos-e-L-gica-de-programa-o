import pandas as pd

# Passo 1: Importar base de dados

tabela = pd.read_csv(r"C:\Users\Gabriel Belo\Downloads\Aula 2\telecom_users.csv")

# Passo 2: Visualizar a base de dados (ver quais informações são "inúteis" e quais são úteis)

# axis = 0 _> linha ou axis = 1 _> coluna
tabela = tabela.drop("Unnamed: 0", axis=1)  # Excluindo essa coluna por ser uma coluna inútil

# Passo 3: Tratamento de dados

# - Valores Vazios (excluir colunas que possuem todas as info vazias e excluir linhas que possuem qualquer info vazia)
# "dropna" - só exclui espaços vazios, how seleciona se deve excluir se tiver um espaço em branco ou todos

tabela = tabela.dropna(how="all", axis=1)
tabela = tabela.dropna(how="any", axis=0)

# Passo 4: Análise Inicial

print(tabela.info())  # Informa todos os dados presentes na tabela
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))  # Mostrar a porcentagem de cancelamento

# Passo 5: Análise Final
import plotly.express as px  # Biblioteca para construção de gráficos (https://plotly.com/python/histograms/)

# Primeiro cria o grafico

for coluna in tabela.columns:  # Fazer um comparativo dos cancelamentos com as outras colunas
    grafico = px.histogram(tabela, x=coluna, color="Churn", text_auto=True)

# Depois exibe o gráfico
    grafico.show()
