# Implemente um programa para calcular o número de arranjos de n objetos diferentes, onde r objetos são escolhidos de cada vez. 

from math import factorial

while True:
    n_objetos_diferentes = int(input('Informe o valor de "n" que são os objetos diferentes: '))
    r_objetos_escolhidos = int(input('Informe o valor de "r" que são os objetos escolhidos: '))

    if n_objetos_diferentes < 0 or r_objetos_escolhidos < 0:
        print('ERRO! Os valores de "n" e "r" não podem ser negativos')
    elif n_objetos_diferentes < r_objetos_escolhidos:
        print('ERRO! O valor de "n" não pode ser menor que o valor de "r"')
    else:
        resultado_arranjo = factorial(n_objetos_diferentes) // factorial(n_objetos_diferentes - r_objetos_escolhidos)
        print(f'\nO resultado do arranjo é: {resultado_arranjo}')
        break
