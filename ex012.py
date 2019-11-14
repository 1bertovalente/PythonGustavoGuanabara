prod = float(input('Valor do produto R$'))

desconto = prod - (prod * (5/100))

print('Valor do produto com desconto R${:.2f}'.format(desconto))
