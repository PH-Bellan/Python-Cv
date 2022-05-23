"""Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120"""
print('Calculo de fatorial')
numero = int(input('Digite um numero: '))
cont = numero
multiplicador = 1
print('{}!'.format(numero))
while cont > 0:
    print('{}'.format(cont), end="")
    print(' x ' if cont > 1 else ' = ', end='')
    multiplicador *= cont
    cont -= 1
print('{}'.format(multiplicador))
