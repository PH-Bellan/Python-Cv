def almentar(n, taxa):
    n = (n * taxa)/100 + n
    return n


def diminuir(n, taxa):
    n = n - (n * taxa)/100
    return n


def dobro(n):
    n *= 2
    return n


def metade(n):
    n /= 2
    return n


def resumo(valor, almento, reducao):
    x = ('=' *35)
    print(x)
    print(f'{"RESUMO DO VALOR":^35}')
    print(x)
    print(f'{"Preço real:":<25}R${valor:.2f}'.replace('.', ','))
    print(f'{"O dobro:":<25}R${dobro(valor):.2f}'.replace('.', ','))
    print(f'{"A metade:":<25}R${metade(valor):.2f}'.replace('.', ','))
    print(f'{f"Com {almento}% de almento:":<25}', end='')
    print(f'R${almentar(valor, almento):.2f}'.replace('.', ','))
    print(f"{f'Com {reducao}% de desconto:':<25}", end='')
    print(f"R${diminuir(valor, reducao):.2f}".replace('.', ','))


def num_format(n):
    return f'{n:.2f}'.replace('.', ',')




