""" Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""
n = 0
numero = []


def maior(*num):
    print(f'Analizando os {len(numero)} numeros digitados.', end=' ')
    for a in num:
        for g in a:
            print(g, end=', ')
    print(f'o maior numero é {max(max(num))}')
    numero.clear()


while True:
    while n != 999:
        n = int(input('Número: '))
        if n == 999:
            break
        numero.append(n)
    maior(numero)
    n = 0
