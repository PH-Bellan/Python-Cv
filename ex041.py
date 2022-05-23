""" A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
 e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER"""
anonasc = int(input('Digite o ano de nascimento: '))
from datetime import date
anoatual = date.today().year
idade = anoatual - anonasc
print('O atleta tem {} anos.'.format(idade))
if 9 >= idade >= 0:
    print('O atleta é MIRIM')
elif 14 >= idade >= 10:
    print('O atleta é INFANTIL')
elif 19 >= idade >= 15:
    print('O atleta é JÚNIOR')
elif 25 >= idade >= 20:
    print('O atleta é SÊNIOR')
elif idade > 25:
    print('O atleta é MASTER')


