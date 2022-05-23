"""Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""
pessoas = list()
dados = list()
cont = 0
while True:
    dados.append(input('Nome: ').strip().title())
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    sair = input('Deseja continuar? [S/N]').strip().title()[0]
    if sair in 'N':
        break
print(f'Número de pessoas cadastradas {len(pessoas)}')
print(f'Pessoas acima de 100Kg:', end=' ')
for p in pessoas:
    if p[1] >= 100:
        print(p, end=' ')
print(f'\nPessoas abaixo de 60Kg:', end=' ')
for p in pessoas:
    if p[1] <= 60:
        print(p, end=' ')




