"""Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
 diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções."""
from uteis import moeda
numero = int(input('Digite o valor: R$ '))
taxa = float(input('Digite a taxa em porcentagem: '))
print(f'Com almento de {taxa:.0f}% de R${numero:.2f} é R${moeda.almentar(numero, taxa):.2f}')
print(f'Com desconto de {taxa:.0f}% de R${numero} é R${moeda.diminuir(numero, taxa):.2f}')
print(f'O dobro de R${numero:.2f} é R${moeda.dobro(numero):.2f}')
print(f'A metade de R${numero:.2f} é R${moeda.metade(numero):.2f}')
