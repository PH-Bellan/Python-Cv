""" Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.
"""
from random import randint
x = '=' * 75
cont = 1
maquina = randint(0, 100)
print(x)
print('Olá! estou pensando em um número de 0 a 10, qual número eu estou pensando?')
print(x)
jogador = int(input('Qual é o seu palpite? : '))

if maquina > jogador:
    print('O número que eu estou pensando é MAIOR do que {}'.format(jogador))
elif maquina < jogador:
    print('O número que eu estou pensando é MENOR do que {}'.format(jogador))
while jogador != maquina:
    jogador = int(input('Tente novamente: '))
    cont += 1
    if jogador < maquina:
        print('O número que eu estou pensando é MAIOR do que {}'.format(jogador))
    if jogador > maquina:
        print('O número que eu estou pensando é MENOR do que {}'.format(jogador))
print('VOCÊ ACERTOU!!!! :)')
print('Acertou na {}º tentativa.'.format(cont))
