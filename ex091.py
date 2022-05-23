"""Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado."""
from random import randint
from operator import itemgetter
from time import sleep
ranking = list()
jogadores = dict()
for j in range(1, 5):
    jogadores[f'Jogador{j}'] = randint(1, 6)
print('Valores sorteados: ')
for a, z in jogadores.items():
    print(f'{a}: Jogou o dado....', end=' ')
    sleep(0.5)
    print(z)
    sleep(1)
print('------------------------')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for a, z in enumerate(ranking):
    print(f'{a+1}° LUGAR: {z[0]} com {z[1]}')


