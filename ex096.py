""" Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
retangular (largura e comprimento) e mostre a área do terreno."""


def Area(a, b):
    area = a * b
    print(f'A area do terreno é de {l} x {c} = {area:.2f}m².')


print('Area de um terreno.')
print('-------------------')
l = float(input('Largura: '))
c = float(input('Comprimento: '))
Area(l, c)
