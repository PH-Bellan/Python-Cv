""" Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
"""
numero1 = float(input('Digite um numero: '))
numero2 = float(input('Digite outro numero: '))
if numero1 > numero2:
    print('O numero {} é maior que {}'.format(numero1, numero2))
if numero2 > numero1:
    print('O numero {} é maior que {}'.format(numero2, numero1))
else:
    print('Os numeros digitados são iguais'.format(numero1, numero2))