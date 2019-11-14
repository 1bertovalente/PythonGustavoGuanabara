#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos KM foram percorridos?'))
dias = float(input('Quantos dias você utilizou?'))

pagar = (km * 0.15) + (dias * 60)

print('Você alugou o carro por {:.0f} dias e rodou {:.2f} KM'.format(dias, km))
print('Você deve pagar R${:.2f} pelo aluguel'.format(pagar))
