""" Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente.
Ao final, mostre o conteúdo das três listas geradas."""
lista = []
for l in range(0, 10):
    lista.append(int(input('Digite um número: ')))
print(f'Lista completa de números digitados {sorted(lista)}')
lista_par = []
lista_impar = []
for n in lista:
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)
print(f'Os números impares digitados foram {sorted(lista_impar)}')
print(f'Os números pares digitados foram {sorted(lista_par)}')
