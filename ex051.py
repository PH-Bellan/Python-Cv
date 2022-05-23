""" Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão."""
x = '='*29
print(x)
print('{:^29}'.format('10 TERMOS DE UMA PA'))
print(x)
primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão PA: '))
for r in range(primeiroTermo, primeiroTermo + razao * 10, razao):
    print(r, end=' -> ')
print('FIM')





