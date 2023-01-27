# Leia um numero real qualquer e mostre na tela sua porção imteira.

from math import trunc
n = float(input('Número: '))
print('A porção inteira é {}'.format(trunc(n)))
#tr = trunc(n)
#print('O número inteiro é {}'.format(tr))


'''
OUTRA FORMA DE RESOLVER
import math
n = float(input('Digite um número:  '))
print('Número digitado foi {} e sua porção inteira é {}'.format(n, math.trunc(n)))
'''

''' 
SEM USAR MÓDULOS
n = float(input('Digite um número: '))
print('Porção inteira do número é {}'.format(int(n)))
'''