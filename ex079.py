"""Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""
# criando a lista
numeros_unicos = []
# entrada de dados até, saida
while True:
    numeros_unicos.append(int(input(f'Digite um número: ')))
    sair = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if sair in 'Nn':
        break
# deletando numeros repetidos
for p, n in enumerate(numeros_unicos):
    if numeros_unicos.count(n) > 1:
        del numeros_unicos[p]
# exibindo os numeros
print(f'Todos os numeros unicos digitados', end=' ')
for n in sorted(numeros_unicos):
    print(n, end=' ')
