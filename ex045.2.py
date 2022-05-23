from time import sleep
from random import randint

print('-=-' * 20)
print('{:^60}'.format('GAME JoKenPÔ'))
print('-=-' * 20)
opcoes = ('Pedra', 'Papel', 'Tesora')
maquina = randint(0, 1)
print("""ESCOLHA:
[0] PEDRA
[1] PAPEL
[2] TESOURA""")

jogador = int(input('Digite a sua escolha: '))
if jogador > 2:
    print('Jogada incorreta')
else:
    sleep(1)
    print('Jo')
    sleep(1)
    print('Ken')
    sleep(1)
    print('PÔ')
    print('Você jogou {}'.format(opcoes[jogador]))
    print('A máquina jogou {}'.format(opcoes[maquina]))
    if maquina == jogador:
        print('-=-' * 20)
        print('{:^60}'.format('EMPATE!!!'))
    elif (maquina == 0 and jogador == 1) or\
            (maquina == 1 and jogador == 2) or\
            (maquina == 2 and jogador == 0):
        print('-=-' * 20)
        print('{:^60}'.format('O JOGADOR VENCEU!!!!'))
    else:
        print('-=-' * 20)
        print('{:^60}'.format('A MAQUINA VENCEU!!!'))
    print('-=-'*20)
