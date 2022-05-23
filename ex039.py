"""Faça um programa que leia o ano de nascimento de um jovem e informe,
 de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
 se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""
from datetime import date
anoatual = date.today().year
anonascimento = int(input('Digite o seu ano de nascimento: '))
idade = anoatual - anonascimento
tprestante = 18 - idade
tpatraso = idade - 18
print('Você naceu em {1} e tem {0} anos '.format(idade, anonascimento))
if idade < 18:
    print('Faltam {} anos para você se alistar'.format(tprestante))
    print('Seu ano de alistamento será em {}'.format(tprestante + anoatual))
elif idade > 18:
    print('Já se passaram {} anos do seu alistamento'.format(tpatraso))
    print('Você deveria ter se alistado em {}'.format(anoatual - tpatraso))
else:
    print('Você deverá se alistar nesse ano.')
