""" Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários
em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média"""
pessoas = list()
cadastro = dict()
mulheres = list()
media_idade = soma_idade = 0
while True:
    cadastro['nome'] = input('Nome: ').strip().title()
    while True:
        sexo = input('Sexo: [M/F] ').strip().title()[0]
        if sexo not in 'MF':
            print('Erro! Digite Masculino ou Feminino.')
        else:
            cadastro['sexo'] = sexo
            if cadastro['sexo'] == 'F':
                mulheres.append(cadastro['nome'])
            break
    cadastro['idade'] = int(input('Idade: '))
    soma_idade += cadastro['idade']
    while True:
        sair = input('Deseja continuar? [S/N] ').strip().title()[0]
        if sair in 'SN':
            break
        else:
            print('Erro! Digite corretamente Sim ou Não')
    pessoas.append(cadastro.copy())
    cadastro.clear()
    if sair == 'N':
        break
media_idade = soma_idade / len(pessoas)
print(f'A) Número de pessoas cadastradas: {len(pessoas)}')
print(f'B) Média de idade: {media_idade}')
print(f'C) Lista de mulheres: ', end=' | ')
for m in mulheres:
    print(m, end=' | ')
print(f'\nD) Pessoas com idade acima da média: ', end=' | ')
for p in pessoas:
    for k, i in p.items():
        if k == 'idade' and i > media_idade:
            print(f'{p["nome"]} com {i} anos', end=' | ')
