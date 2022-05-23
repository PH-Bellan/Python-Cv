""": Escreva um programa em Python que leia um número inteiro qualquer
 e peça para o usuário escolher qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal."""
numero = int(input('Digite um número inteiro: '))
print("""Escolha qual tipo de converção você quer fazer
[1] BINARIO
[2] OCTAL
[3] HEXADECIMAL""")
opcao = int(input('DIGITE:'))
if opcao == 1:
    print('O numero {} convertido para BINARIO é {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('O numero {} convertido para OCTAL é {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('O numero {} convertido para HEXADECIMAL é {}'.format(numero, hex(numero)[2:]))
else:
    print('Entrada invalida. digite apenas 1, 2 ou 3.')