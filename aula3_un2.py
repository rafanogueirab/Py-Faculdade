class Pessoa:
    #O código __init__ é um construtor, chamado quando um objeto da classe é criado.
    #Ele inicializa os atributos da classe.
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        #Self é uma convenção em Python que se refere à própria instância da classe.
        #Os parâmetros nome, idade e genero são passados durante a criação do objeto.
        # Eles são usados para inicializar os atributos da instância.

    # O comando cumprimentar retorna uma saudação com o nome da pessoa
    def cumprimentar(self):
        return f"Olá, meu nome é {self.nome}"
    # O comando aniversario aumenta a idade da pessoa em 1.
    def aniversario(self):
        self.idade += 1
# Cria uma instância da classe "Pessoa" com os valores vc que sabe, 30 e "Masculino" para nome, idade e genero, respectivamente.
pessoa1 = Pessoa(input('Digite seu nome: '), 30, 'Masculino')
#Chama o comando "cumprimentar" na instância pessoa1 e imprime a saudação
print(pessoa1.cumprimentar()) #Saída: Olá, meu nome é João
#Acessa o atributo idade da instância pessoa1 e imprime sua idade
print(f"Idade: {pessoa1.idade}")
#Chama o comando aniversario na instância pessoa1 para aumentar sua idade em 1
pessoa1.aniversario()
#Acessa o atributo idade atualizada da instância pessoa1 e imprime sua nova idade.
print(f"Nova Idade: {pessoa1.idade}")