#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math

numero = float(input('numero?'))

print('numero digitado {} numero truncado {}'.format(numero, math.trunc(numero)))
