""" Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada"""
from time import sleep


def contador(a, b, x):
    print('~'*60)
    print(f'Contagem inicia no {a}, termina no {b}, com o espaço de {x}.')
    if x == 0:
        x = 1
    if b < a and x > 0:
        x = x - x - x
    for c in range(a, b, x):
        print(c, end=' ')
        sleep(0.3)
    print('Fim!')


contador(1, 10, 1)
contador(10, 0, -2)
while True:
    inicio = int(input('Número de inicio: '))
    final = int(input('Até:'))
    intervalo = int(input('Qual é o intervalo?: '))
    contador(inicio, final, intervalo)
