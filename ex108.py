""" Adapte o código do desafio #107, criando uma função adicional chamada moeda()
que consiga mostrar os números como um valor monetário formatado.
"""
from uteis import moeda
numero = int(input('Digite o valor: R$ '))
taxa = float(input('Digite a taxa em porcentagem: '))
almento = moeda.almentar(numero, taxa)
desconto = moeda.diminuir(numero, taxa)
dobro = moeda.dobro(numero)
metade = moeda.metade(numero)
print(f'Com almento de {taxa:.0f}% de R${moeda.num_format(numero)} é R${moeda.num_format(almento)}')
print(f'Com desconto de {taxa:.0f}% de R${moeda.num_format(numero)} é R${moeda.num_format(desconto)}')
print(f'O dobro de R${moeda.num_format(numero)} é R${moeda.num_format(dobro)}')
print(f'A metade de R${moeda.num_format(numero)} é R${moeda.num_format(metade)}')
