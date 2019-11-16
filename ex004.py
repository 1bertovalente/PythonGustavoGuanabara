#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

algo = input('Digite algo:')

print('O tipo primitivo é:', type(algo), '\nSó tem espaços?', algo.isspace(), '\nÉ um número?',
      algo.isnumeric(), '\nÉ alfabetico?', algo.isalpha(),'\nÉ alfanúmerio?', algo.isalnum(),
      '\nEstá em maiúscula?', algo.isupper(),'\nEstá em minúscula?', algo.islower(),'\nEstá capitalizada?',
      algo.istitle())
