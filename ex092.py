"""Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o
(com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá
também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos
a pessoa vai se aposentar.
"""
from datetime import date
pessoa = dict()
pessoa['nome'] = input('Nome: ').strip().title()
nascimento = int(input('Ano de nascimento: '))
pessoa['idade'] = date.today().year - nascimento
print('Se não tiver carteira, digite [ 0 ]')
pessoa['carteira de trabalho'] = int(input('N° Carteira de trabalho: '))
if pessoa['carteira de trabalho'] == 0:
    print(f'- {pessoa["nome"]}')
    print(f'- {pessoa["idade"]} anos')
    print('- Não possue carteira de trabalho.')
else:
    pessoa['ano contratação'] = int(input('Ano da primeira contratação: '))
    pessoa['primeiro salario'] = float(input('Primeiro salário: '))
    tempo_restante = 35 - (date.today().year - pessoa['ano contratação'])
    pessoa['idade aposentadoria'] = tempo_restante + pessoa['idade']
    print(f'- {pessoa["nome"]}')
    print(f'- {pessoa["idade"]} anos')
    print(f'- Contratado em {pessoa["ano contratação"]}, com o salário de R${pessoa["primeiro salario"]:.2f}')
    print(f'- {pessoa["nome"]} tem estimativa de se aposentar com {pessoa["idade aposentadoria"]} anos.')
