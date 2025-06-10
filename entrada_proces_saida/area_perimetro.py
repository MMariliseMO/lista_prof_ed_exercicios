#Escreva um programa para determinar a área e o perímetro de um retângulo.

base = float(input('Informe o valor da base do retângulo: '))
altura = float(input('Informe o valor da altura do retângulo: '))

area = base * altura
perimetro = 2 * (base + altura)

print(f'A área do retângulo é: {area :.1f}')
print(f'O perímetro do retângulo é: {perimetro :.1f}')