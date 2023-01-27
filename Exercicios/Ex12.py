# LEIA O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE O NOVO SALÁRIO COM +15% DE AUMENTO.

n = float(input('SALÁRIO: R$ '))
aumento = n * (15/100)
aumentado = n + aumento

print('AUMENTO NO SALÁRIO: R$ {} \n SALÁRIO COM AUMENTO: R$ {}'.format(aumento, aumentado))