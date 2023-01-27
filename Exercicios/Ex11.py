# FAÇA UM PROGRAMA QUE MOSTRE 5% DE DESCONTO EM CIMA DE UM VALOR QUALQUER.

n = float(input('VALOR DO PRODUTO: R$ '))
desconto = n * (5/100)
descontado = n - desconto
print(' VALOR DESCONTADO: {:.2f} \n VALOR C/ DESCONTO: {:.2f}'.format(desconto, descontado))