""" Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""
from time import sleep
opcao = 0
n1 = float(input('Informe um número: '))
n2 = float(input('Informe outro número: '))
while opcao != 5:
    print('====================')
    opcao = int(input("""Digite a opção
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair
--> """))
    if opcao == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print('O maior é o {}'.format(n1))
        else:
            print('O maior é o {}'.format(n2))
    elif opcao == 4:
        print('Informe novos números')
        n1 = float(input('Informe um número: '))
        n2 = float(input('Informe outro número: '))
    elif opcao == 5:
        print('Finalizando......')
    elif opcao > 5 or opcao < 1:
        print('Opção invalida.')
    print('====================')
    sleep(3)
print('FIM')
