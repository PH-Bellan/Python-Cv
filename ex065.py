""" Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""
maior = menor = cont = total = 0
continuar = sair = ''
while sair in 'Nn':
    n = int(input('Digite um número: '))
    if cont == 0:
        maior = n
        menor = n
    else:
        if menor > n:
            menor = n
        if maior < n:
            maior = n
    total += n
    cont += 1
    continuar = input('Deseja continuar [S/N]: ')
    if continuar in 'Nn':
        media = total / cont
        print('Foram digitados {} números, a média dos numeros digitados é {:.2f}.'.format(cont, media))
        print('O maior numero digitado foi {} e o menor {}'.format(maior, menor))
        sair = input('Deseja sair? [S/N]: ')
print('FIM')
