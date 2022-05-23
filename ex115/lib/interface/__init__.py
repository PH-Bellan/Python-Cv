def linha(tam=42):
    return '-' * tam


def cabecalho(msg):
    print(linha())
    print(f'{msg:^42}')
    print(linha())


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'O valor digitado não é valido.')
            continue
        else:
            return n


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    for num, op in enumerate(lista):
        print(f'{num + 1} - {op}')
    print(linha())
    while True:
        escolha = leiaInt('Sua escolha: ')
        try:
            return escolha, lista[escolha - 1]
        except IndexError:
            print(f'Opção {escolha} invalida, digite uma opção valida.')
            continue
