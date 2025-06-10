#Dados os pontos A, de coordenadas A(x₁, y₁) e B(x², y²), escreva um programa que determine a distância entre os dois pontos.

#coordenadas A
a_x = float(input('Informe o valor da coordenada A no ponto x: '))
a_y = float(input('Informe o valor da coordenada A no ponto y: '))

#coordenadas B
b_x = float(input('Informe o valor da coordenada B no ponto x: '))
b_y = float(input('Informe o valor da coordenada B no ponto y: '))

print('\n-_-_- Cálculo da distância -_-_-\n')

distancia = (((b_x - a_x) ** 2) + ((b_y - a_y) ** 2)) ** 0.5
print(f'A distância entre as coordenadas é de: {distancia :.1f}')