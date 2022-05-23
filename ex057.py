""" Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto."""
sexo = input('Informe o seu sexo [M/F] ').strip().upper()[0]
while sexo not in 'MF':
    sexo = input('Informação invalida, informe o seu sexo novamente. [M/F]: ').strip().upper()[0]
print('Sexo {} registrada com sucesso.'.format(sexo))
