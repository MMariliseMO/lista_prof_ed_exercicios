# Fazer um programa para receber 5 valores inteiros do usuário e mostrar a sua média (que pode não ser inteira).

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))
num5 = int(input("Digite o quinto número: "))

soma = (num1 + num2 + num3 + num4 + num5)
media = (num1 + num2 + num3 + num4 + num5) / 5

print(f'A soma dos números é: {soma} e a média é: {media :.1f}')

#usando o for
soma = 0

for i in range(5):
    num = int(input(f'Digite o {i+1}º número: '))
    soma += num

media = soma / 5

print(f'A soma dos números é de: {soma} e a média é de: {media :.1f}')
