""" Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo. """
while True:
    n = int(input('Digite um número e veja a sua tabuada\nOU digite um numero NEGATIVO para sair: '))
    if n < 0:
        break
    for d in range(0, 11):
        print(f'{n} x {d:2} = {n*d}')
print('fim....')
