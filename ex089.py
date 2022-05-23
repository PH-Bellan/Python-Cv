""" Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
de cada aluno individualmente."""
lista = []
nome_aluno = []
nota_aluno = []
while True:
    nome_aluno.append(input('Nome: ').strip().title())
    nota_aluno.append(float(input('Nota 1: ')))
    nota_aluno.append(float(input('Nota 2: ')))
    nome_aluno.append(nota_aluno[:])
    lista.append(nome_aluno[:])
    nome_aluno.clear()
    nota_aluno.clear()
    sair = input('Deseja continuar? ').strip().title()[0]
    if sair in 'N':
        break
print('='*50)
print(f'{"BOLETIM":^50}')
print('='*50)
for n in lista:
    print(f'NOME: {n[0]:<30} ', end=' ')
    print(f'MÉDIA: {(n[1][0]+n[1][1])/2}')
print('='*50)
while True:
    nota_detalhada = input('Nota detalhada [S/N] ').strip().title()
    if nota_detalhada in 'S':
        nome = input('Digite o nome do aluno: ').strip().title()
        for n in lista:
            if nome in n[0]:
                print(f'Aluno: {n[0]:<20}', end=' ')
                print(f'Nota 1: {n[1][0]}', end=' ')
                print(f'Nota 2: {n[1][1]}', end=' ')
                print()
    else:
        break



