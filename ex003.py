filmes = ['Trovão Tropical', 'Interestelar', 'A Bruxa', 'Invocação do Mal', 'As Branquelas']

print('Bem-vindo ao Letterboxd de baixa renda!')
print('Classifique os filmes com até 5 estrelas.')
print('A qualquer momento digite "0" para parar. \n')

for filme in filmes:
    rank =  input(f'Nota para {filme}: ')

    if rank == '0':
        print('Então tá bão...')
        break

    rank = int(rank)

    if rank < 1 or rank > 5:
        print('Bota uma nota válida né bonzão!')
    else:
        print(f'Nota para {filme} foi {rank}!')

print('Valeu e até a próxima!')