"""Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""
from datetime import date
Dmenor = 0
Dmaior = 0
for pessoas in range(1, 8):
    ano = int(input('Qual é o ano de nacimento da {}º pessoa:'.format(pessoas)))
    idade = date.today().year - ano
    if idade < 18:
        Dmenor += 1
    else:
        Dmaior += 1
print('{} pessoas menores de idade.'.format(Dmenor))
print('{} pessoas maiores de idade.'.format(Dmaior))

