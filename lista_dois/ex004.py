# Escreva um programa que leia uma letra e verifique se ela é uma vogal ou uma consoante.

vogais = ('a', 'e', 'i', 'o', 'u')
letra = str(input('Informe uma letra qualquer, seja vogal ou consoante: ')).lower()

if letra in vogais:
    print(f'"{letra}" é uma vogal')
else:
    print(f'"{letra}" é uma consoante')