nome = input('Digite o seu nome completo:').strip()
nomedividido = nome.split()
print('Seu nome em maiusculo é {}'.format(nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
print('O seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
print('O seu primeiro nome tem {} letras'.format(len(nomedividido[0])))





