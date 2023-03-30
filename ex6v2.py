preço = float(input('informe o preço unitario do produto: '))
quant = float(input('informe a quantidade de produtos: '))
percent = float(input('informe o percentual de desconto(%)'))

valortotal = (quant * preço) * (1 - percent /100)

print(f'o valor total do produto é de R$ {valortotal:.2f} ')
