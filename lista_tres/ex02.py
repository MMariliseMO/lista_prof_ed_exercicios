#Programa que verifica se um número é par ou ímpar

num = int(input('Informe um número: '))

if num % 2 == 0:
    print(f'O número {num} é par')
else:
    print(f'O número {num} é ímpar')