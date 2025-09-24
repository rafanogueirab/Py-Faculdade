#atualizar produto
import sqlite3
#Conectando banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()
# Novo preço e ID do produto a ser atualizado
novo_preco = 24.99
produto_id = 1 # Suponhamos que queremos atualizar o produto com ID 1
# Comando SQL para atualizar o preço do produto
atualizar_preco = "UPDATE Produtos SET preco = ? WHERE id = ?"
# Executando o comando SQL de atualização
cursor.execute(atualizar_preco, (novo_preco, produto_id))
# Confirmando as alterações
conn.commit()
# Fechando a conexão
conn.close()