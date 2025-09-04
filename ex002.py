# Programa dos filmes

# Solicitando idade do cliente

idade = int(input('Informe sua idade: '))

if 0 < idade <= 12:
    print('Recomendamos para você o filme "Superman"!')
elif 12 < idade < 18:
    print('Recomendamos para você o filme "Interestelar"!')
elif 18 <= idade <= 99:
    print('Recomendamos para você o filme "A Hora do Mal"!')
else:
    print('Idade inválida.')

