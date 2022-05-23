"""Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer
 e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8"""
print('Sequência de Fibonacci')
n = int(input('Quantos termos você quer exibir? '))
termo = 3
primeiro = 0
segundo = 1
print(primeiro, '<', segundo, end=' < ')
while termo <= n:
    terceiro = primeiro + segundo
    print(terceiro, end=' < ')
    primeiro = segundo
    segundo = terceiro
    termo += 1
print('END')
