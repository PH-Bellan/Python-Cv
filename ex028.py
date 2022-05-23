""" Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
from random import randint
from time import sleep
print('-=-'*30)
print('Olá!!! Vou pensar em um número de 0 a 5, tente adivinhar qual número eu estou pensando.')
print('-=-'*30)
sleep(1)
numero = randint(0, 5)
palpite = int(input('Qual é o seu palpite? '))
print('loading....')
sleep(2)
if palpite == numero:
    print('Você acertou :) O numero que eu pensei foi o {}'.format(numero))
else:
    print('Você errou :( O numero que eu pensei foi o {}'.format(numero))
print('Obrigado por jogar!!!')

