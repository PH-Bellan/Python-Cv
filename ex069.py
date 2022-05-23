"""Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. """
cont18 = conthomem = contmulher20 = 0
while True:
    idade = int(input('IDADE: '))
    while True:
        sexo = input('SEXO [M/F] ')
        if sexo in 'Mm':
            sexo = 'masculino'
            break
        elif sexo in 'Ff':
            sexo = "feminino"
            break
        elif sexo not in 'MmFf':
            sexo = ''
    if idade > 18:
        cont18 += 1
    if sexo == 'masculino':
        conthomem += 1
    if idade < 20 and sexo == 'feminino':
        contmulher20 += 1
    continuar = input('Continuar? [S/N]')
    if continuar in "nN":
        break
print(f'{cont18} pessoas tem mais que 18 anos.\n'
      f'{conthomem} homens foram cadastrados\n'
      f'{contmulher20} mulheres tem menos que 20 anos.')
