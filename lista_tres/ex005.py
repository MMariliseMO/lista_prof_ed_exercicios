#Programa que verifica se uma pessoa é adulta, adolescente ou criança

idade = int(input('Informe a idade: '))

if idade < 12:
    print('Criança')
elif idade >= 12 and idade < 18:
    print('Adolescentes')
else:
    print('Adulto')