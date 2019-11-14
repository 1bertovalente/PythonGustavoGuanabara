#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input('Informe a temperatura em Graus Celsius:'))

fahrenheit = (celsius * (9/5) + 32)

print('{}ºC é equivale a {}ºF'.format(celsius, fahrenheit))
