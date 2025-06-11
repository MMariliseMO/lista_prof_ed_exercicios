#Programa que verifica se um número é perfeito

num = int(input('Informe um número inteiro positivo: '))

soma_divisores = 0
if num <= 0:
    print(f'O número {num} não é um inteiro positivo.')
else:
    for i in range(1, num):
        if num % i == 0:
            soma_divisores += i
            print(f'O número {num} é um número perfeito')

if soma_divisores == num:
    print(f'O número {num} É um número perfeito!')
else:
    print(f'O número {num} NÃO é um número perfeito.')