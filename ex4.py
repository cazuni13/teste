#Escreva um algoritmo que leia uma temperatura em graus Fahrenheit e a converta para graus
#Celsius, cuja fórmula de conversão é: C = (F - 32) / 1.8


fahrenheit = float(input('informe a temperatura em fahrenheit: '))

celcius = (fahrenheit-32) / 1.8

print(f'a temperatura em graus celcius fica: {celcius: .2f}')
