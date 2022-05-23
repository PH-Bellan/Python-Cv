""": Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""
lista = []
while True:
    numero = int(input('Digite um numero: '))
    lista.append(numero)
    sair = input('Deseja CONTINUAR? [S/N] ')
    if sair in 'nN10':
        break
print(f'{len(lista)} números foram digitados')
lista.sort(reverse=True)
print(f'Lista em ordem decrescente: {lista}')
if 5 in lista:
    print('O número 5 ESTÁ na lista.')
else:
    print('O número 5 NÃO ESTÁ na lista')

