#Escreva um algoritmo que leia uma temperatura em graus Celsius e a converta para graus
#Fahrenheit, cuja fórmula de conversão é: F = C *1.8 + 32.


celcius = float(input('informe a temperatura em graus celsius (°C): '))

fahrenheit = celcius * 1.8 + 32

print(f'a temperatura convertida para fahrenheit (°F) fica: {fahrenheit:.2f}')
