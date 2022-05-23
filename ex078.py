""" Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
# criando a lista
numero = []
# input do usuário
for n in range(0, 5):
    numero.append(int(input(f'Digite o número da posição {n} ')))
# print da lista
for n in numero:
    print(f'{n}', end=' ')
# print do maior numero e posições
print(f'\nO maior número digitado foi {max(numero)} na posição', end=' ')
for p, n in enumerate(numero):
    if n == max(numero):
        print(p, end=' ')
# print do menor numero e posições
print(f'\nO menor número digitado foi {min(numero)} na posição', end=' ')
for p, n in enumerate(numero):
    if n == min(numero):
        print(p, end=' ')
