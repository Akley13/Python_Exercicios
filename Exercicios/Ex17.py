#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
#de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import hypot
co = float(input('CATETO OPOSTO: '))
ca = float(input('CATETO ADJACENTE: '))
hi = hypot(co, ca)
print('A hipotenusa é {:.2f}'.format(hi))

'''
SEM MÓDULO
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa é {:.2f}'.format(hi))
'''