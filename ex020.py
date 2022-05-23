from random import shuffle
a1 = input('Nome do aluno1: ')
a2 = input('Nome do aluno2: ')
a3 = input('Nome do aluno3: ')
a4 = input('Nome do aluno4: ')
Aluno = [a1, a2, a3, a4]
shuffle(Aluno)
print('A ordem de apresentação do trabalho é: {}'.format(Aluno))
