#excluir produto
import sqlite3
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()
#ID do produto a ser excluído
produto_id = 1 #Suponhamos que queremos excluir o produto com ID 2
# Comando SQL para excluir o produto
excluir_produto = "DELETE FROM produtos WHERE id = ?"
#Executando o comando SQL de exclusão
cursor.execute(excluir_produto, (produto_id,))
#Confirmando alterações
conn.commit()
#Fechando a conexão
conn.close()