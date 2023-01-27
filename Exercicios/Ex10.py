# LEIA QUANTOS R$ O INDIVIDUO TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELE PODE COMPRAR.

n = float(input('Valor na Carteira R$ '))

c = n / 5.17

print('Com R$ {} você terá U$ {:.2f}'.format(n, c))