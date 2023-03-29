valorinicial = float(input('informe o valor inicial: '))
dias = int(input('informe os dias de atraso: '))

multa = dias * 5/100
valorfinal = valorinicial + valorinicial * multa

print(valorfinal)
