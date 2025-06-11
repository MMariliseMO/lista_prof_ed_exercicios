#Programa que verifica se um número é par, ímpar ou positivo

num = int(input('Informe um número qualquer: '))

if num > 0:
    if num % 2 == 0:
        print(f'O número {num} é par e positivo')
    else:
        print(f'O número {num} é ímpar e positivo')
elif num < 0:
    if num % 2 == 0:
        print(f'O número {num} é negativo e par.')
    else:
        print(f'O número {num} é negativo e ímpar.')
else:
    print(f'O número {num} é zero (e é considerado par).')