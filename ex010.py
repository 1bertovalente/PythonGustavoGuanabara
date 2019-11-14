real = float(input('Valor em R$:'))

#Considere dolar a 3,27
dolar = real / 3.27

print('Com R${:.2f} você comprar ${:.2f}'.format(real,dolar))

