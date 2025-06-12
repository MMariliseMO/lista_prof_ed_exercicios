#Sejam a e b os catetos de um triângulo retângulo cuja hipotenusa h é obtida pela equação: (h = raiz(a² + b²)). Faça um programa que leia os valores de a e b, e calcule o valor da hipotenusa através da fórmula dada. Imprima o resultado

cateto_a = float(input('Informe o valor do cateto a: '))
cateto_b = float(input('Informe o valor do cateto b: '))

hipotenusa = (cateto_a ** 2 + cateto_b ** 2) ** 0.5

print(f'O valor da hipotenusa é: {hipotenusa :.1f}')
