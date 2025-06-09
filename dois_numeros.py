#Ler dois números e informar o dividendo, o divisor, o quociente e o resto do primeiro pelo segundo e do segundo pelo primeiro

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))

print('\n*-*-*-*- Dividindo o 1º Número pelo 2º Número -*-*-*-*\n')

if num2 != 0:
    dividendo1 = num1
    divisor1 = num2
    quociente1 = num1 // num2 #para o quociente ficar inteiro //
    resto1 = num1 % num2

    print(f'O dividendo é: {dividendo1}')
    print(f'O divisor é: {divisor1}')
    print(f'O quociente é: {quociente1}')
    print(f'O resto é: {resto1}')
else:
    print("O número é igual a 0 e não pode dividir por zero.")

print('\n*-*-*-*- Dividindo o 2º Número pelo 1º Número -*-*-*-*\n')

if num1 != 0:
    dividendo2 = num2
    divisor2 = num1
    quociente2 = num2 // num1 #para o quociente ficar inteiro //
    resto2 = num2 % num1

    print(f'O dividendo é: {dividendo2}')
    print(f'O divisor é: {divisor2}')
    print(f'O quociente é: {quociente2}')
    print(f'O resto é: {resto2}')
else:
    print("O número é igual a 0 e não pode dividir por zero.")