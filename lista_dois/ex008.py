#Crie uma aplicação para calcular o IMC (Índice de Massa Corporal) que leia o peso do usuário em quilogramas e a altura em metros e que depois calcule e apresente o IMC. Além disso, o programa deverá exibir as informações seguintes do Ministério da Saúde para que a pessoa possa avaliar seu IMC: VALORES DE IMC Abaixo do peso: menor que 18,5 Normal: entre 18,5 e 24,9 Acima do peso: entre 25 e 29,9 Obeso: 30 ou mais

peso = float(input('Informe o peso em quilogramas: '))
altura = float(input('Informe a altura em metros ex: 1.68: '))

imc = peso / (altura * altura) 
print('\n-=-=-=- Interpretação do IMC -=-=-=-')
print('''
Abaixo do peso: menor que 18,5 
Normal: entre 18,5 e 24,9 
Acima do peso: entre 25 e 29,9 
Obeso: 30 ou mais\n''')

if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <= 24.9:
    print('Peso normal')
elif imc >= 25 and imc <= 29.9:
    print('Acima do peso')
else:
    print('Obeso')