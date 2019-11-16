#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

a1 = input('Nome do aluno')
a2 = input('Nome do aluno')
a3 = input('Nome do aluno')
a4 = input('Nome do aluno')

alunos = [a1, a2, a3, a4]

escolhido = random.choice(alunos)

print('O aluno escolhido foi {}'.format(escolhido))
