from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cadastro.txt'
if arquivoExiste(arq):
    print('Arquivo encontrado.')
else:
    print('Arquivo NÃO encontrado.')
    criarArquivo(arq)


while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar pessoas', 'Sair'])
    sleep(1)
    if resposta[0] == 1:
        cabecalho(resposta[1])
        lerArquivo(arq)
    elif resposta[0] == 2:
        cabecalho(resposta[1])
        nome = input('Nome: ').strip().title()
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta[0] == 3:
        print('Fim do programa...')
        break
    sleep(2)

