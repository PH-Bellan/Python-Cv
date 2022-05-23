"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""
cont = 0
numero = (int(input('Digite um número: ')), int(input('Outro número:')),
          int(input('Mais um número:')), int(input('Último número:')))
for n in numero:
    print(n, end=' ')
print(f'\nO número 9 apareceu {numero.count(9)} vezes.')
if 3 in numero:
    print(f'O número 3 apareceu na posição {numero.index(3)+1}.')
for n in range(0, 4):
    if numero[n] % 2 == 0:
        cont += 1
if cont > 0:
    print('Os numeros pares são:', end=' ')
    for n in range(0, 4):
        if numero[n] % 2 == 0:
            print(numero[n], end=' ')
else:
    print('Nenhum numero par foi digitado')
    