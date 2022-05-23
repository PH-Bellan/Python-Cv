""" Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o."""
soma = 0
cont = 0
for a in range(1, 7):
    numero = int(input('Digite o {}º número: '.format(a)))
    if numero % 2 == 0:
        soma += numero
        cont += 1
print('A soma dos {} numeros PARES digitados é = {}'.format(cont, soma))



