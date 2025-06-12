#Dados os pontos A, de coordenadas A(x1, y1) e B de coordenadas B(x2, y2) , escreva um programa que determine a distância entre os dois pontos. Considere que: distância = raiz(x2 - x1)² + (y2 - y1)²

#coordenadas A
a_x = float(input('Informe o valor da coordenada A no ponto x: '))
a_y = float(input('Informe o valor da coordenada A no ponto y: '))

#coordenadas B
b_x = float(input('Informe o valor da coordenada B no ponto x: '))
b_y = float(input('Informe o valor da coordenada B no ponto y: '))

print('\n-_-_- Cálculo da distância -_-_-\n')

distancia = (((b_x - a_x) ** 2) + ((b_y - a_y) ** 2)) ** 0.5
print(f'A distância entre as coordenadas é de: {distancia :.1f}')