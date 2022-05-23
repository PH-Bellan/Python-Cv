def arquivoExiste(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
        print(f'Novo arquivo - {arq}')
    except:
        print('Houve um erro!')

def lerArquivo(arq):
    try:
        a = open(arq, 'rt')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '' )
            print(f'Nome: {dado[0]:<30}{dado[1]:>3} anos.')
    except:
        print('Erro ao exibir o arquivo.')

def cadastrar(arq, nome='desconhecido', idade = 0):
    try:
        a = open(arq, 'at')
    except:
        print('Ocorreu um problema ao tentar abrir o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
            print(f'{nome} cadastrado com sucesso.')
        except:
            print('Ocorreu um problema ao tentar escrever no arquivo')