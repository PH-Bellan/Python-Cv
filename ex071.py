""": Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues."""
total = cedula50 = cedula20 = cedula1 = 0
saque = int(input('Valor a ser sacado: R$'))
while True:
    if saque >= 50:
        saque -= 50
        cedula50 += 1
    elif saque >= 20:
        saque -= 20
        cedula20 += 1
    elif saque >= 1:
        saque -= 1
        cedula1 += 1
    if saque == 0:
        break
if cedula50 > 0:
    print(f'{cedula50} cedulas de R$50.00')
if cedula20 > 0:
    print(f'{cedula20} cedulas de R$20.00')
if cedula1 > 0:
    print(f'{cedula1} cedulas de R$1.00')
