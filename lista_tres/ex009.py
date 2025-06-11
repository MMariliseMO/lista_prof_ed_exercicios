#Programa que verifica se um número é divisível por outro número

num1 = int(input('Informe um número qualquer: '))
num2 = int(input('Informe outro número qualquer: '))

if num2 == 0:
    print(f'Não é permitido a divisão por 0')
elif num1 % num2 == 0:
    print(f'O número {num1} é divisível por {num2}')
else:
    print(f'O número {num1} não é divisível por {num2}')