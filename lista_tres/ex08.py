#Programa que verifica se uma pessoa tem altura suficiente para andar em um brinquedo de parque de diversões (a altura mínima é digitada pelo usuário)

altura_minima = float(input('Informe a altura mínima exigida pelo brinquedo: '))

altura_pessoa = float(input('Informe a altura da pessoa: '))

if altura_pessoa >= altura_minima:
    print('Liberada! A pessoa tem a altura mínima exigida para andar no brinquedo.')
else:
    print('A pessoa não tem a altura mínima exigida para andar no brinquedo.')