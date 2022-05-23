"""Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela."""
alunos = dict()
alunos['nome'] = input('Nome: ').strip().title()
alunos['media'] = float(input('Média: '))
if alunos['media'] >= 5:
    alunos['situação'] = 'Aprovado'
else:
    alunos['situação'] = 'Reprovado'
print(f'- Nome: {alunos["nome"]}')
print(f'- Média: {alunos["media"]}')
print(f'- {alunos["nome"]} está: {alunos["situação"]}')
