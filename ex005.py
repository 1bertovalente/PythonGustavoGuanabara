#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número: '))

antecessor = n - 1
sucessor = n + 1

print('Atecessor: {}\nSucessor: {}'.format(antecessor,sucessor))
