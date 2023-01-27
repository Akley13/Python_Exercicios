# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km_percorrido = float(input("KM'S PERCORRIDOS: "))
dias_alugados = int(input('DIAS ALUGADOS: '))
km = km_percorrido * 0.15
dias = dias_alugados * 60
total = km + dias

print('O preço a pagar por km rodado é R$ {}. E o valor do aluguel por dia é R$ {}. \nTOTALIZANDO R$ {}'.format(km, dias, total))
