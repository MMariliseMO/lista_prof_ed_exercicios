# Considere que se dispõe de um capital x que rende j% de juros ao ano. Escreva um programa que leia x e j e mostre o capital acumulado com o juros ao final de n anos. (Juros compostos)

capital = float(input('Informe o capital: R$ '))
taxa_juros = str(input('Informe a taxa de juros: ')).replace('%', '')
anos = int(input('Em quantos anos deseja manter a aplicação? '))

taxa_juros_limpa = float(taxa_juros)
taxa_juros_final = taxa_juros_limpa / 100 
montante = capital * (1 + taxa_juros_final) ** anos

print(f'O capital acumulado depois de {anos} anos é: {montante :.1f}')


