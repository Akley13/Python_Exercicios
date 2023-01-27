# sorteie 4 alunos para o professor.

from random import choice
a1 = str(input('ALUNO 1: '))
a2 = str(input('ALUNO 2: '))
a3 = str(input('ALUNO 3: '))
a4 = str(input('ALUNO 4: '))
lista = [a1, a2, a3, a4]
sorteado = choice(lista)
print('O aluno escolhido foi {}'.format(sorteado))
