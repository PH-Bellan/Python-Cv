#Programa que verifica se tem 'silva' no nome do usuario
nome = input('Digite o seu nome: ').strip()
nome = nome.lower()
print('Seu nome tem Silva? {}'.format('silva' in nome))

