#Elaborar programa que lê os coeficientes a, b e c de uma equação de segundo grau e, antes de calcular as raízes, calcula o delta. Se este for negativo, informe que a equação não tem solução real. Se for zero, mostra a única raiz. Se positivo, mostra as duas raízes.

from math import sqrt
a = float(input('Informe o valor de "a": '))
b = float(input('Informe o valor de "b": '))
c = float(input('Informe o valor de "c": '))

delta = b ** 2 - 4 * a * c 

if delta < 0:
    print('Equação sem solução real.')
elif delta == 0:
    raiz_unica = -b / (2 * a)
    print(f'A equação possui uma única raiz real: {raiz_unica :.1f}')
else:
    raiz1 = (-b + (sqrt(delta))) / (2 * a)
    raiz2 = (-b - (sqrt(delta))) / (2 * a)
    print(f'A raiz 1 é de: {raiz1 :.1f}')
    print(f'A raiz 2 é de: {raiz2 :.1f}')