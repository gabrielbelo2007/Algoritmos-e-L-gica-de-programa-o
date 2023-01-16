# IA para previsão de vendas

# Passo 1: Entendimento do Desafio
# Passo 2: Entendimento da Área/Empresa
# Passo 3: Extração/Obtenção de Dados

import pandas as pd

tabela = pd.read_csv(r"C:\Users\Gabriel Belo\Downloads\Aula 4\advertising.csv")
print(tabela)

# Passo 4: Ajuste de Dados (Tratamento/Limpeza)

# Passo 5: Análise Exploratória (Analisar a correlação de cada item)

import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(tabela.corr(), annot=True, cmap="Wistia")
plt.show()

# outra forma de ver a mesma análise
# sns.pairplot(tabela)
# plt.show()


# Passo 6: Modelagem + Algoritmos (Aqui que entra a Inteligência Artificial, se necessário)
# Treinando a IA a partir dos dados que ja existem, vendo se ela consegue prever o real resultado

from sklearn.model_selection import train_test_split

y = tabela["Vendas"]
x = tabela.drop("Vendas", axis=1)

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)

# Dois métodos de adivinhação para a IA, arvore de decisão e regressão linear, teste para saber qual é melhor

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

# cria as inteligencias artificiais
modelo_regressaolinear = LinearRegression()
modelo_arvoredecisao = RandomForestRegressor()

# treina as inteligencias artificias
modelo_regressaolinear.fit(x_treino, y_treino)
modelo_arvoredecisao.fit(x_treino, y_treino)

# Descobrindo qual o melhor método

from sklearn import metrics

# criar as previsões
previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)

# comparar os modelos
print(metrics.r2_score(y_teste, previsao_regressaolinear))
print(metrics.r2_score(y_teste, previsao_arvoredecisao))

# Passo 7: Interpretação de Resultados
# Visualizar os gráficos das previsões

tabela_auxiliar = pd.DataFrame()
tabela_auxiliar["y_teste"] = y_teste
tabela_auxiliar["Previsoes ArvoreDecisao"] = previsao_arvoredecisao
tabela_auxiliar["Previsoes Regressao Linear"] = previsao_regressaolinear

plt.figure(figsize=(15, 6))
sns.lineplot(data=tabela_auxiliar)
plt.show()

# Fazer uma nova previsão

nova_tabela = pd.read_csv(r"C:\Users\Gabriel Belo\Downloads\Aula 4\novos.csv")
print(nova_tabela)
previsao = modelo_arvoredecisao.predict(nova_tabela)
print(previsao)
