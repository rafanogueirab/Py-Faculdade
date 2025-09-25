import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

conn = sqlite3.connect('dados_vendas.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas1 (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    data_venda DATE,
    produto TEXT,
    categoria TEXT,
    valor_venda REAL
    )
''')

cursor.execute("SELECT COUNT(*) FROM vendas1")
if cursor.fetchone()[0] == 0:
    cursor.execute('''
    INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda) VALUES
    ('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
    ('2023-01-05', 'Produto B', 'Roupas', 350.00),
    ('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
    ('2023-03-15', 'Produto D', 'Livros', 200.00),
    ('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
    ('2023-04-02', 'Produto F', 'Roupas', 400.00),
    ('2023-05-05', 'Produto G', 'Livros', 150.00),
    ('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
    ('2023-07-20', 'Produto I', 'Roupas', 600.00),
    ('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
    ('2023-09-30', 'Produto K', 'Livros', 300.00),
    ('2023-10-05', 'Produto L', 'Roupas', 450.00),
    ('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
    ('2023-12-20', 'Produto N', 'Livros', 250.00);
    ''')
conn.commit()


df_vendas = pd.read_sql('SELECT * FROM vendas1', conn)
df_vendas["data_venda"] = pd.to_datetime(df_vendas["data_venda"])

print("Primeiros dados: \n", df_vendas.head())

print("\n Informações do DataFrame:")
print(df_vendas.info())

print("\n Estatísticas descritivas:")
print(df_vendas.describe())

df_vendas['mes'] = df_vendas['data_venda'].dt.month
df_vendas['ano'] = df_vendas['data_venda'].dt.year

vendas_categoria = df_vendas.groupby('categoria')['valor_venda'].sum().reset_index()
print('\n Vendas totais por categoria:')
print(vendas_categoria)

vendas_mes = df_vendas.groupby('mes')['valor_venda'].sum().reset_index()
print('\n Vendas totais por mês:')
print(vendas_mes)

top_produto = df_vendas.loc[df_vendas['valor_venda'].idxmax()]
print(f'\n Produto de maior valor de venda: {top_produto["produto"]} ({top_produto["valor_venda"]})')
print(top_produto)

sns.set_style('whitegrid')

plt.figure(figsize=(8,5))
sns.barplot(x='categoria', y='valor_venda', data=df_vendas, estimator=sum, errorbar=None, palette='Set2')
plt.title('Vendas totais por categoria')
plt.ylabel('Total de vendas (R$)')
plt.show()

plt.figure(figsize=(10,5))
sns.lineplot(x='mes', y='valor_venda', data=df_vendas, estimator=sum, errorbar=None, marker='o')
plt.title('Vendas totais por mês')
plt.xlabel('Mês')
plt.ylabel('Total de vendas (R$)')
plt.xticks(range(1,13))
plt.show()

print("\n Conclusões e Insights:")
print("- A categoria **Eletrônicos** gerou o maior volume de vendas.")
print("- Há picos de vendas em Janeiro, Março e Novembro, possivelmente relacionados a sazonalidade (Ano Novo, volta às aulas, Black Friday).")
print("- Produtos de maior ticket médio estão em Eletrônicos.")
print("- Livros e Roupas têm vendas menores, mas podem ser explorados em promoções ou combos para aumentar o ticket médio.")