"""Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla."""
from random import randint
numeros = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
for n in numeros:
    print(n, end=' ')
print(f'\nO MENOR número foi {min(numeros)}.\nO MAIOR numero foi {max(numeros)}.')
