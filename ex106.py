""" Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
Importante: use cores."""


def ajuda():
    PyHelp = ' '
    while PyHelp != 'fim':
        PyHelp = input('Digite o comando em Python: ').strip().lower()
        if PyHelp == 'fim':
            print('Fim do programa!')
        else:
            print(help(PyHelp))


ajuda()
