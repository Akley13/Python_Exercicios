# sorteie 4 alunos e mostre uma ordem de apresentação.

from random import shuffle
a1 = input('ALUNO 1: ')
a2 = input('ALUNO 2: ')
a3 = input('ALUNO 3: ')
a4 = input('ALUNO 4: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ORDEM É ', lista)