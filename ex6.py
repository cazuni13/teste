# Escreva um programa que calcule o preço final de uma venda, a partir do preço unitário do
# produto, a quantidade vendida e o percentual de desconto

preço = float(input('informe o preço unitario do produto: '))
quant = float(input('informe a quantidade de produtos: '))
percent = float(input('informe o percentual de desconto(%)'))

total = preço * quant
print(f'o total sem desconto é de R$ {total:.2f}, mas com {percent} % de desconto')

valortotal = total - (total * percent /100)
print(f'o valor total do produto é de R$ {valortotal:.2f} ')
