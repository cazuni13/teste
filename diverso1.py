empregados = int(input('informe a quantidade de funcionários da empresa: '))
dias = int(input('informe a quantidade de dias que irão durar: '))

marmitas = dias * empregados
print('esta empresa tem um total de', marmitas, 'marmitas')

empregadosadd = int(input('informe quantos empregados foram contratados: '))

empregadostotais = empregadosadd + empregados
dias = marmitas / empregadostotais

print('ira durar', dias, 'dias')
