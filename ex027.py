#com a entrada de um nome, o programa identifica o primeiro nome e o ultimo
nome = input('Digite o seu nome completo: ').strip().title()
print('É um prazer te conhecer {}!'.format(nome.split()[0]))
print('O seu primeiro nome é {}'.format(nome.split()[0]))
print('O seu ultimo nome é {}'.format(nome[nome.rfind(' ')+1:]))






