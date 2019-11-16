#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

an = float(input('Digite o angulo: '))

seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tan = math.tan(math.radians(an))

print('Seno {:.2f}\nCosseno {:.2f}\nTangente {:.2f}'.format(seno, cosseno, tan))
