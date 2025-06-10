#Faça um programa que leia 4 valores reais (a, b, c e d) e determine: A média aritmética; A média harmônica (MH); A média geométrica (MG); A média quadrática (MQ).

a = float(input('Informe o valor de "a": '))
b = float(input('Informe o valor de "b": '))
c = float(input('Informe o valor de "c": '))
d = float(input('Informe o valor de "d": '))

print('\n*-*- Cálculo da média aritmética -*-*\n')

media = (a + b + c + d) / 4
print(f'A média aritmética é: {media :.1f}')

print('\n*-*- Cálculo da média harmônica -*-*\n')
if a == 0 or b == 0 or c == 0 or d == 0:
    print('Não é possível calcular a média harmônica com 0.')
else:
    mh = 4 / ((1 / a) + (1 / b) + (1 / c) + (1 / d))
    print(f'A média harmônica é: {mh :.1f}')

print('\n*-*- Cálculo da média geométrica -*-*\n')
if a < 0 or b < 0 or c < 0 or d < 0:
    print('Não é possível calcular média geométrica com valores negativos. ')
else:
    mg = (a * b * c * d) ** 0.25
    print(f'A média geométrica é: {mg :.1f}')

print('\n*-*- Cálculo da média quadrática -*-*\n')

mq = ((a ** 2 + b ** 2 + c ** 2 + d ** 2) / 4) ** 0.5
print(f'A média quadrática é: {mq :.1f}')


