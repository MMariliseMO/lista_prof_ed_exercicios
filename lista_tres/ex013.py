#Programa que verifica se um número é primo ou não e, em caso afirmativo, exibe todos os seus divisores

num = int(input('Informe um número qualquer: '))

if num < 2:
    print(f'O número {num} não é primo!')
else:
    divisores = [] #lista vazia para armazenar os divisores
    
    for i in range(2, num):
        if num % i == 0:
            divisores.append(i)

    if len(divisores) == 0:
        print(f'{num} é primo!')
        print(f'Seus divisores são: 1 e {num}')
    else:
        print(f'{num} não é primo!')
        print(f'Seus divisores além de 1 e {num} são: {divisores}')