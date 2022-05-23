""" Crie um programa onde o usuário possa digitar sete valores numéricos e
cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente."""
lista_numerica = [[], []]
for n in range(0, 7):
    numero = int(input(f'{n+1}º número: '))
    if numero % 2 == 0:
        lista_numerica[0].append(numero)
    else:
        lista_numerica[1].append(numero)
print(f'Os valores PARES digitados foram: {sorted(lista_numerica[0])}')
print(f'Os valores IMPARES digitados foram: {sorted(lista_numerica[1])}')
