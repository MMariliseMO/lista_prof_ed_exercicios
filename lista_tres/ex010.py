#Programa que verifica se um número é primo

num = int(input('Informe um número qualquer: '))

if num < 2:
    print(f'Não é primo!')
else:
    eh_primo = True #começamos assumindo que o número é primo. Por isso, precisamos realizar testes
    for i in range (2, num): #o for serve para testar os números de 2 até o número anterior ao digitado
        if num % i == 0:  
            eh_primo = False #se na divisão o resto for 0, encontramos um dividor. Então não é primo 
            break
if eh_primo:
    print(f'{num} é primo!')
else:
    print(f'{num} não é primo!')