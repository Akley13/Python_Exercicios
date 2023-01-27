'''
Leia a largura e altura em metros, calcule a área e a quantidade de tinta necessária para pinta-la,
sabendo que cada litro de tinta, pinta uma área de 2m²
'''

larg = float(input('LARGURA: '))
alt = float(input('ALTURA: '))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))