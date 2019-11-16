#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metro = float(input('Informe distancia em metros: '))

cm = metro * 100
mm = metro * 1000

print('Metros informados {} corresponde a :\n{:.0f} cm e {:.0f} mm'.format(metro, cm, mm))
