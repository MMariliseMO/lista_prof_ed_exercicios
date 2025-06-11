#Implemente um programa para calcular o número de combinações de n objetos diferentes, onde r objetos são escolhidos de cada vez.

from math import comb
while True:
    n_objetos_diferentes = int(input('Informe o valor de "n" que é o total de objetos diferentes: '))
    r_objetos_escolhidos = int(input('Informe o valor de "r" que é o total de objetos escolhidos: '))

    if n_objetos_diferentes < 0 or r_objetos_escolhidos < 0:
        print('ERRO! O número de "n" e de "r" não podem ser negativos.')
    elif n_objetos_diferentes < r_objetos_escolhidos:
        print('ERRO! O número de "n" não pode ser menor que o número de "r".')
    else:
        resultado_combinacao = comb(n_objetos_diferentes, r_objetos_escolhidos)
        print(f'\nO número de combinações é de: {resultado_combinacao}')
        break


