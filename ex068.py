"""Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. """
import random
cont = 0
while True:
    maquina = random.randint(0, 10)
    while True:
        jogador = int(input("Digite um número de 0 a 10: "))
        if 0 <= jogador <= 10:
            break
        else:
            print('Jogada invalida.')
    while True:
        parImpar = input('Escolha Par ou Impar [P/I]: ')
        if parImpar in 'Pp':
            parImpar = 'Par'
            maquinaparImpar = 'Impar'
            break
        elif parImpar in 'Ii':
            parImpar = 'Impar'
            maquinaparImpar = 'Par'
            break
        elif parImpar not in 'IiPp':
            parImpar = ''
    resultado = (maquina + jogador) % 2
    if resultado == 1 and parImpar == 'Impar':
        print(f'JOGADOR {jogador}, {parImpar}')
        print(f'MÁQUINA {maquina}, {maquinaparImpar}')
        print(f'{maquina + jogador} IMPAR.')
        print('O JOGADOR VENCEU!!!!')
        cont += 1
    elif resultado == 0 and parImpar == 'Par':
        print(f'JOGADOR {jogador}, {parImpar}')
        print(f'MÁQUINA {maquina}, {maquinaparImpar}')
        print(f'{maquina + jogador} PAR.')
        print('O JOGADOR VENCEU!!!!')
        cont += 1
    else:
        break
print('A máquina venceu!!')
print(f'Você ganhou {cont} em sequência.')
