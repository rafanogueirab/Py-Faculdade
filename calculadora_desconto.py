#calculadora de desconto com ordem de parada
def calculo_desconto(valor, desconto):
    valor_final = valor - (valor * (desconto / 100))
    return valor_final

print('\nBem-vindo a calculadora de desconto! Caso queira encerrar as atividades, digite "0".')

while True: #ao utilizar esse while true, o loop fica infinito até quebrar com o "0" no valor do produto.
    valor = float(input('Digite o valor do produto: '))

    if valor == 0:
        print('Atividade encerrada.')
        break

    desconto = float(input('\nDigite o percentual de desconto: '))

    if desconto < 0 or desconto > 100:
        print('Digite um percentual de desconto entre 0 e 100.\n')
    else:
        print(f'\nO valor final do produto é: {calculo_desconto(valor, desconto):.2f}\n')

print('Obrigado por usar o programa.')