#Programa que verifica se um número é positivo, negativo ou zero

num = int(input('Informe um número qualquer: '))

if num < 0:
    print('Número negativo!')
elif num == 0:
    print('Número é 0!')
else:
    print('Número positivo!')