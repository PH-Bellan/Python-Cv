""" Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação
de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade."""


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'O valor digitado não é valido.')
            continue
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'O valor digitado não é valido.')
            continue
        else:
            return n


while True:
    numeroInt = leiaInt('Digite um numero inteiro: ')
    numeroFloat = leiaFloat('Digite um numero real: ')
    try:
        resultado = numeroInt / numeroFloat
    except ZeroDivisionError:
        print('Não é possivel dividir por zero')
        continue
    else:
        print(f'{numeroInt} dividido por {numeroFloat} = {resultado}')


