import matplotlib.pyplot as plt

class Livro:
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Gênero: {self.genero}, Quantidade: {self.quantidade}"

biblioteca = []

def cadastrar_livro(titulo, autor, genero, quantidade):
    livro = Livro(titulo, autor, genero, quantidade)
    biblioteca.append(livro)
    print(f'Livro {titulo} adicionado com sucesso!')

def listar_livros():
    if not biblioteca:
        print('Nenhum livro cadastrado ainda.')
    else:
        for livro in biblioteca:
            print(livro)

def buscar_livro(titulo):
    for livro in biblioteca:
        if livro.titulo.lower() == titulo.lower():
            return livro
    return None

def gerar_grafico():
    if not biblioteca:
        print('Nenhum livro cadastrado para gerar gráfico.')
        return

    generos = {}
    for livro in biblioteca:
        generos[livro.genero] = generos.get(livro.genero, 0) + livro.quantidade

    plt.bar(generos.keys(), generos.values())
    plt.xlabel('Gênero')
    plt.ylabel('Quantidade de Livros')
    plt.title('Quantidade de Livros por Gênero')
    plt.show()

cadastrar_livro("Dom Casmurro", "Machado de Assis", "Romance", 5)
cadastrar_livro("O Hobbit", "J.R.R. Tolkien", "Fantasia", 3)
cadastrar_livro("1984", "George Orwell", "Ficção", 4)
cadastrar_livro("O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia", 2)

print("\nLista de livros:")
listar_livros()

print("\nBuscando livro '1984':")
livro = buscar_livro("1984")
print(livro if livro else "Livro não encontrado.")

print("\nGerando gráfico...")
gerar_grafico()