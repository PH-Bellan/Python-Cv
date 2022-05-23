""" Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
 a soma entre todos os valores pares sorteados pela função anterior."""
from random import randint
numeros = list()


def sorteia():
    for n in range(0, 5):
        numeros.append(randint(0, 10))
    print(f'Os numeros sorteados foram {numeros}.')


def somarPar():
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f'A soma de todos os numeros pares é {soma}.')


sorteia()
somarPar()
            