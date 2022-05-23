""" Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta."""
from random import randint
from time import sleep
mega_sena = list()
jogo = list()
print('='*39)
print(f'{"MEGA SENA":^39}')
print('='*39)
jogos = int(input('Quantos jogos você quer fazer? '))
numero_jogos = 1
while jogos >= numero_jogos:
    cont = 0
    while True:
        numero = randint(0, 60)
        if numero not in jogo:
            jogo.append(numero)
            cont += 1
        if cont == 6:
            break
    jogo.sort()
    mega_sena.append(jogo[:])
    jogo.clear()
    numero_jogos += 1
for numero_do_jogo, j in enumerate(mega_sena):
    print(f'Jogo {numero_do_jogo+1}: | ', end='')
    for n in j:
        print(f'{n:^2}', end=' | ')
    print()
    sleep(0.5)
print('='*39)
print(f'{"BOA SORTE!!!":^39}')
print('='*39)
