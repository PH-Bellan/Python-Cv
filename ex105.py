"""Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e
vai retornar um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione também as docstrings dessa função para consulta pelo desenvolvedor."""


def notas(*n, sit=False):
    total = 0
    for nota in n:
        total += nota
    media = dict()
    media['qtd.notas'] = len(n)
    media['maior'] = max(n)
    media['menor'] = min(n)
    media['média'] = total / len(n)
    if media['média'] >= 7.5:
        situacao = 'BOA'
    elif 7.5 > media['média'] >= 5:
        situacao = 'RAZOAVEL'
    else:
        situacao = 'RUIM'
    if sit:
        media['situação'] = situacao
    print(media)
    return situacao


resp = notas(10, 1.6, 3.4, 7, 8, 4, sit=True)
print(resp)
