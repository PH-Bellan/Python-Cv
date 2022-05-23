""" Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while."""
print('Gerador PA')
inicio = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão PA: '))
cont = 0
soma = razao + inicio
while cont != 10:
    if cont == 0:
        print(inicio, end=' < ')
    elif 0 < cont < 9:
        print(soma, end=' < ')
        soma += razao
    elif cont == 9:
        print(soma)
    cont += 1
print('FIM....')
