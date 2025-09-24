import pandas as pd

#Criar um dicionário com nome e idade
dados = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Idade': [25, 30, 22, 35, 28]
}
#Criar uma série a partir do dicionário
series_idade = pd.Series(dados['Idade'], index = dados['Nome'])

#Exibir série de idades
print("Série de idades:")
print(series_idade)
#Calcular a média das idades
media_idades = series_idade.mean()
print("\nMédia de idades:", media_idades)
