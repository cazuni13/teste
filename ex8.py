# Escreva um programa que determine o número de dias e de horas que uma pessoa já viveu.
# Considere que um mês tem 30 dias.

idade = int(input('informe sua idade: '))

dias = idade * 360
horas = dias * 24

print(f'você ja viveu {dias} dias e {horas} horas.')
