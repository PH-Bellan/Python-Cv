"""Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o
ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem
 voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições."""
from datetime import date


def voto(ano):
    """
    -> Função que lê o ano de nascimento de uma pessoa e informa se o voto é negado, obrigatorio ou opcional
    :param ano: ano de nascimento
    :return: situação de voto[0], idade[1]
    """
    idade = date.today().year - ano
    if idade < 16:
        s = 'NEGADO'
    elif idade == 17 or idade == 18 or idade > 65:
        s = 'OPCIONAL'
    else:
        s = 'OBRIGATÓRIA'
    return s, idade


nascimento = int(input('Ano nascimento: '))
situacao = voto(nascimento)

print(f'Você tem {situacao[1]} anos e sua situação eleitoral é {situacao[0]}.')
