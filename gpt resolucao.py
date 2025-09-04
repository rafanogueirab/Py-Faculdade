filmes = ['Trovão Tropical', 'Interestelar', 'A Bruxa', 'Invocação do Mal', 'As Branquelas']

print('Bem-vindo ao Letterboxd de baixa renda!')
print('Classifique os filmes com até 5 estrelas.')
print('A qualquer momento digite "0" para parar. \n')

for filme in filmes:
    while True:  # Repete até a entrada ser válida
        rank = input(f'Nota para {filme}: ')

        if rank == '0':
            print('Então tá bão...')
            filmes = []  # Força saída do loop externo
            break

        if not rank.isdigit():  # Garante que o valor seja numérico
            print('Digite um número válido!')
            continue

        rank = int(rank)

        if rank < 1 or rank > 5:
            print('Bota uma nota válida né bonzão!')
        else:
            print(f'Nota para {filme} foi {rank}!')
            break  # Sai do while e vai para o próximo filme

    if not filmes:  # Se lista estiver vazia, para o for
        break

print('Valeu e até a próxima!')
