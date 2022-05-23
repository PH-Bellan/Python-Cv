""" Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
 só que agora utilizando um laço for."""
numero = int(input('Digite um numero e veja a tabuada: '))
print('-x' * 7)
print('{:^12}'.format('TABUADA DO {}'.format(numero)))
print('-x' * 7)
for n in range(1, 11):
    print(' {:2} X {} = {}'.format(n, numero, n * numero))
print('-x' * 7)




