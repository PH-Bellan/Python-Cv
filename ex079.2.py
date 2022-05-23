"""Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""
# criando a lista
numeros_unicos = []
# entrada de dados
while True:
    numero = int(input(f'Digite um número: '))
    if numero not in numeros_unicos:
        print(f'O número {numero} foi salvo com sucesso!!!')
        numeros_unicos.append(numero)
    else:
        print(f'O Número {numero} já está cadastrado.')
# saida do programa
    sair = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if sair in 'Nn':
        break
# exibir os numeros na tela
print('Os número salvos são ', end='')
for n in sorted(numeros_unicos):
    print(n, "...", end='')
