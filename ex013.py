#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Informe o salario R$'))

reajuste = salario + (salario * (15/100))

print('Valor do salario com reajuste de 15% é de: R${:.2f}'.format(reajuste))
