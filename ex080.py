"""Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela."""
lista_numerica = []
for n in range(0, 5):
    numero = int(input('Digite um número: '))
    if n == 0 or numero > lista_numerica[-1]:
        lista_numerica.append(numero)
    else:
        cont = 0
        while cont < len(lista_numerica):
            if numero <= lista_numerica[cont]:
                lista_numerica.insert(cont, numero)
                break
            cont += 1
print(lista_numerica)
