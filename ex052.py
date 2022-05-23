""" Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""
numero = int(input('Digite um número: '))
cont = 0
for a in range(1, numero + 1):
    if numero % a == 0:
        print('\033[32m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(a), end=' ')
if cont == 2:
    print('\n\033[mO número {} É PRIMO'.format(numero))
else:
    print('\n\033[mO número {} NÃO É PRIMO'.format(numero))
