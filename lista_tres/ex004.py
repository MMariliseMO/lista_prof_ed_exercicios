#Programa que verifica se um número está dentro de um intervalo (digitado pelo usuário)

num = int(input('Informe um número qualquer: '))

while True: 
    inicio = int(input('Qual o início do intervalo? '))
    final = int(input('Qual o final intervalo? '))

    if inicio <= final:
        break
    else:
        print(f'O início não pode ser maior que o final.')

if num >= inicio and num <= final:
    print(f'O número {num} está dentro do intervalo.')
else:
    print(f'O número {num} não está dentro do intervalo.')