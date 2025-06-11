#Programa que verifica se um número é múltiplo de 3 ou de 5

num = int(input('Informe um número qualquer: '))

if num % 3 == 0 or num % 5 == 0:
    print(f'O número {num} é múltiplo de 3 ou de 5')
else:
    print(f'O número {num} não é múltiplo 3 ou de 5')
