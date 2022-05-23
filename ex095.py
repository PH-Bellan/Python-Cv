"""Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um
 sistema de visualização de detalhes do aproveitamento de cada jogador."""
jogadores = list()
gols = list()
jogador = dict()
x = '='*40
while True:
    jogador['nome'] = input('Nome: ').strip().title()
    partidas = int(input('Número de partidas jogadas: '))
    for p in range(0, partidas):
        gols.append(int(input(f'Gols {p+1}° partida: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    gols.clear()
    jogador.clear()
    while True:
        continuar = input('Deseja continuar? [S/N]: ').strip().title()[0]
        if continuar in 'SN':
            break
        else:
            print('Apenas SIM ou NÂO.')
    if continuar == 'N':
        break
print(x)
print(f'{"Cod."}|{"Nome":<20}|{"Gols":<20}')
for n, jogador in enumerate(jogadores):
    print(f'{n+1:<4}|{jogador["nome"]:<20}|{jogador["gols"]}|  Total - {jogador["total"]}')
print(x)
while True:
    cod = int(input('Digite o Codigo do jogador para mostrar os dados detalhados: '))
    cod -= 1
    for n, jogador in enumerate(jogadores):
        if n == cod:
            print(jogador['nome'])
            print(x)
            for n, gol in enumerate(jogador['gols']):
                print(f'{n+1}° Partida - {gol} Gols ')
