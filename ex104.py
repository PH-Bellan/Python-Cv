"""Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')"""


def leiaInt(msg):
    while True:
        x = input(msg).strip()
        if x.isnumeric():
            valor = int(x)
            break
        else:
            print('\033[0;31mErro! Digite um numero valido\033[m')
    return valor


while True:
    n = leiaInt('Digite um número: ')
    print(f'Você digitou o número {n}')
