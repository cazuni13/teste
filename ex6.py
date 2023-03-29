preço = float(input('informe o preço unitario do produto: '))
quant = float(input('informe a quantidade de produtos: '))
percent = float(input('informe o percentual de desconto(%)'))

total = preço * quant
valortotal = (total) - (total) * percent / 100

print('o valor total do produto é de', valortotal)
