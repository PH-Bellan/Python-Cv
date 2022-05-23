numero = int(input('Digite um número:'))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print('Analizando o número {} ele tem:'.format(numero))
print('Unidades: {}'.format(u))
print('Dezenas: {}'.format(d))
print('Centenas: {}'.format(c))
print('Milhar: {}'.format(m))

