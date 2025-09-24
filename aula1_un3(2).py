import sqlite3
#vizualizar produto
# Conectando ao banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()
# Comando SQL para selecionar todos os produtos
selecionar_produtos = "SELECT * FROM produtos"
# Executando o comando SQL
cursor.execute(selecionar_produtos)
# Obtendo todos os registros e exibindo-os
produtos = cursor.fetchall()
for produto in produtos:
    print(produto)
# Fechando a conexão
conn.close()