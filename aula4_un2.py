import matplotlib.pyplot as plt

#Dados
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 5]

#Criar gráfico de linha
plt.bar(x,y)

#Adicionar rótulos aos eixos
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')

#Adicionar um título ao gráfico
plt.title('Exemplo de gráfico de linha')

#Mostrar gráfico
plt.show()