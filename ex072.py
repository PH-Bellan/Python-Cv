"""Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso."""
numero = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE',
          'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')
while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if n < 0 or n > 20:
            print('Tente novamente.', end=' ')
        else:
            break
    print(f'O número digitado foi {n} ({numero[n]}) ')
    sair = input('Deseja continuar? ')
    if sair in 'Nn':
        break
print('Fim do programa....')
