#Fazer um algoritmo para receber um número inteiro de segundos do usuário e imprimir a quantidade correspondente em horas, minutos e segundos.

segundos_totais = int(input('Informe os segundos: '))

horas = segundos_totais // 3600
segundos_reto = segundos_totais % 3600
minutos = segundos_reto // 60
segundos_finais = segundos_reto % 60

print(f'\n{segundos_totais} segundos, equivale a: \n')
print(f'{horas} horas')
print(f'{minutos} minutos')
print(f'{segundos_finais} segundos')

print(f'{horas}:{minutos}:{segundos_finais}')

