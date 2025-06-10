#Ler um valor em reais e exibir o equivalente em dólares. A cotação do dia é inserida pelo usuário.

valor_real = float(input('Informe o valor em reais: R$'))

cotacao_dolar = float(input('Informe a cotação do dólar: '))

valor_dolar = valor_real / cotacao_dolar

print(f'O valor R${valor_real} em dólar é: US${valor_dolar :.2f}')