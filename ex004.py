# calculo de media com funções

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
nota4 = float(input('Quarta nota: '))

notas = [nota1, nota2, nota3, nota4]

def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

arredondar_media = lambda media: round(media, 2)

media = calcular_media(notas)
media_arredondada = arredondar_media(media)

situacao = "Aprovado" if media >= 7 else "Reprovado"

print('Notas do estudante: ', notas)
print('Média arredondada: ', media_arredondada)
print('Situação do estudante: ', situacao)