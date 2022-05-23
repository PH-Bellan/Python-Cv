"""Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois
vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
será guardado em um dicionário, incluindo o total de gols feitos durante
o campeonato"""
jogador = dict()
gols = list()
total = 0
x = ('='*30)
jogador['nome'] = input('Nome: ').strip().title()
partidas = int(input('Número de partidas: '))
for p in range(0, partidas):
    g = int(input(f'Gols marcados na {p+1}° partida:'))
    gols.append(g)
    total += g
jogador['gols'] = gols
jogador['total'] = total
print(x*2)
print(jogador)
print(x*2)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
for k in jogador.keys():
    if k == 'gols':
        for p, g in enumerate(jogador["gols"]):
            print(f'{p+1}° Partida: {g} gols')
print(x)
print(f'TOTAL DE GOLS: {jogador["total"]}')
