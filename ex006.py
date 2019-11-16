#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('valor: '))

dobro = n * 2
triplo = n * 3
raiz = n**(1/2)

print('Dobro: {}\nTriplo: {}\nRaiz: {}'.format(dobro,triplo,raiz))
