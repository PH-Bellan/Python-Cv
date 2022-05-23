""" Crie um programa que faça o computador jogar Jokenpô com você."""
from time import sleep
from random import randint

print('-=-' * 20)
print('{:^60}'.format('GAME JoKenPÔ'))
print('-=-' * 20)
print("""ESCOLHA:
[1] PEDRA
[2] PAPEL
[3] TESOURA""")
escolhajogador = int(input('Qual é a sua opção: '))
escolhamaquina = randint(1, 3)
sleep(1)
if escolhajogador > 3:
    print('Somente PEDRA PAPEL TESOURA')
if escolhajogador == 1 or escolhajogador == 2 or escolhajogador == 3:
    print('Jo')
    sleep(1)
    print('Ken')
    sleep(1)
    print('PÔ')
    sleep(1)
    print('-=-' * 20)
    if (escolhajogador == 1 and escolhamaquina == 1) or \
            (escolhajogador == 2 and escolhamaquina == 2) or \
            (escolhajogador == 3 and escolhamaquina == 3):
        print('{:^60}'.format('EMPATE!!!'))
        print('-=-' * 20)
    elif (escolhajogador == 1 and escolhamaquina == 3) or \
            (escolhajogador == 2 and escolhamaquina == 1) or \
            (escolhajogador == 3 and escolhamaquina == 2):
        print('{:^60}'.format('O JOGADOR VENCEU: PICA DAS GALÁXIAS!!!'))
    else:
        print('{:^60}'.format('A MAQUINA VENCEU HAHAHAHAHAH!!!'))
        print('-=-' * 20)
