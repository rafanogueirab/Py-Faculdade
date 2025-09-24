import pandas as pd
#Criando um DataFrame com 5 linhas de dados
data = {
    'nome': ['Produto A', 'Produto B', 'Produto C', 'Produto A', 'Produto E'],
    'quantidade de itens comprados': [3,1,4,3,2],
    'tipo de item': ['Eletrônico', 'Vestuário', 'Alimento', 'Eletrônico', 'Alimento'],
    'receita total': [120,80,60,120,90]
}
df = pd.DataFrame(data)

df.drop_duplicates(keep='last', inplace=True)
print(df)

df['preço do item'] = df['receita total'] / df['quantidade de itens comprados']

itens_acima_de_50 = df[df['preço do item'] > 50]

print("\nItens acima de 50 reais:")
print(itens_acima_de_50)