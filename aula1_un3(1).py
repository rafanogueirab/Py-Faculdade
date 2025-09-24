#Adicionar produto
import sqlite3
#Conectando ao banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()
#Dados do novo produto
novo_produto = ('Camiseta', 39.99, 50)
#Comando SQL para inserir o novo produto na tabela
inserir_produto = "INSERT INTO Produtos (nome, preco, estoque) VALUES (?, ?, ?)"
#Executando o comando SQL para inserção
cursor.execute(inserir_produto, novo_produto)
#Confirmando as alterações
conn.commit()
#Fechando a conexão
conn.close()

