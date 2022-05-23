""": Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = soma_3 = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'[linha {l+1} coluna {c+1}] Número: '))
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
        if c == 2:
            soma_3 += matriz[l][c]
        if l == 1:
            if c == 0:
                maior = matriz[l][c]
            else:
                if matriz[l][c] > maior:
                    maior = matriz[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f"{matriz[l][c]:^5}", end=' | ')
    print()
print(f'A soma de todos os numeros pares é {soma_par}')
print(f'A soma de todos os numeros da terceira coluna é {soma_3}')
print(f'O maior valor da segunda linha é {maior}')
