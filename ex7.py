# Uma loja deseja calcular o preço final a ser cobrado por uma duplicata. Esta loja aplica uma
# multa de 5% do valor da duplicata para cada dia de atraso.

valorinicial = float(input('informe o valor inicial: '))
dias = int(input('informe os dias de atraso: '))

multa = dias * 5/100
valorfinal = valorinicial + valorinicial * multa

print(f' o valor vinal é de {valorfinal} reais')
