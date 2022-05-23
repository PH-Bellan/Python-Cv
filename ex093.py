"""Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois
vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
será guardado em um dicionário, incluindo o total de gols feitos durante
o campeonato."""
jogador = dict()
gols = 0
jogador['nome'] = input('Nome: ').strip().title()
partidas = int(input('Número de partidas: '))
for p in range(0, partidas):
    jogador[f'Partida {p+1}'] = int(input(f'Gols marcados na {p+1}° partida:'))
print('='*30)
print(f'Jogador {jogador["nome"]} ')
for p, g in jogador.items():
    if p != 'nome':
        print(f'{p}: {g} Gols marcados.')
        gols += g
else:
    gols = gols
print('='*30)
print(f'Saldo total de gols: {gols}')






