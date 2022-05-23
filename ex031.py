""" Desenvolva um programa que pergunte a distância de uma viagem em Km.
 Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
"""
km = float(input('Qual é a distancia que a viagem vai percorrer? '))
if km > 200:
    print('A passagem vai custar R${:.2f}.'.format(km * 0.45))
else:
    print('A passagem vai custar R${:.2f}.'.format(km * 0.5))
print('Obrigado por escolher viajar com a gente!!!')



