#Leia uma velocidade em km/h (quilômetros por hora) e apresente convertida em m/s (metros por segundo). A fórmula de conversão é M = K / 3.6, sendo K a velocidade em km/h e M em m/s

velocidade_km = float(input("Informe a velocidade em km/h: "))

metro = velocidade_km / 3.6

print(f'A velocidade {velocidade_km} em m/s é de: {metro :.2f} m/s.')