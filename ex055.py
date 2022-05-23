"""Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos."""
maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input('Digite o peso da {}º pessoa. Kg '.format(pessoa)))
    if pessoa == 1:
        menor = peso
        maior = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
print('O maior peso digitado foi Kg {}'.format(maior))
print('O menor peso digitado foi Kg {}'.format(menor))

