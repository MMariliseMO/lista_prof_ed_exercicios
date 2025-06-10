# Sejam a e b os catetos de um triângulo retângulo cuja hipotenusa h é obtida pela equação: h igual a raiz quadrada de a ao quadrado mais b ao quadrado fim da raiz. Faça um programa que leia os valores de a e b, e calcule o valor da hipotenusa através da fórmula dada. Imprima o resultado.

#através da fórmula
a = float(input("Digite o valor do cateto 'a': "))
b = float(input("Digite o valor do cateto 'b': "))

hipotenusa = (a**2 + b**2) ** 0.5

print(f'O valor da hipotenusa dos catetos {a} e {b} é de: {hipotenusa :.1f}')


#importei a biblioteca match.hypot
from math import hypot

a = float(input("Digite o valor do cateto 'a': "))
b = float(input("Digite o valor do cateto 'b': "))

hipotenusa = hypot(a, b)

print(f'O valor da hipotenusa dos catetos {a} e {b} é de: {hipotenusa :.1f}')