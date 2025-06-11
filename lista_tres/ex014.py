#Programa que verifica se uma pessoa é alta o suficiente para jogar basquete (a altura é digitada pelo usuário)

altura_usuario = float(input('Informe a sua altura (ex: 1.68): '))
altura_ideal_basquete = float(input('Qual a altura ideal para jogar basquete? '))

if altura_usuario >= altura_ideal_basquete:
    print(f'A altura {altura_usuario} está dentro do permitido para jogar basquete')
else:
    print(f'A altura {altura_usuario} não está dentro do permitido para jogar basquete')