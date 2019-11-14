#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math

co = float(input('Cateto Oposto? '))
ca = float(input('Cateto adjacente'))

resp = math.hypot(co, ca)

print('{:.2f}'.format(resp))
