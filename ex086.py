""" Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta."""
matriz = []
dados = []
for n in range(1, 10):
    dados.append(int(input(f'{n}° Número: ')))
    matriz.append(dados[:])
    dados.clear()
print('='*12)
print(f'{"MATRIZ 3x3":^12}')
print('='*12)
for p, n in enumerate(matriz):
    if p == 3 or p == 6:
        print(f'\n{n}', end=' ')
    else:
        print(f'{n}', end=' ')
