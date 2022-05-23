#programa que identifica quantas letras 'A' aparecem em uma frase, e informa a posição da primeira letra 'A' e ultima
frase = input('Escreva uma frase: ').strip()
frase = frase.lower()
print('A letra A aparece {} vezes na frase.'.format(frase.count('a')))
print('A primeira letra A aparece na posição {}'.format(frase.find('a')+1))
print('A ultima letra A aparece na posição {}'.format(frase.rfind('a')+1))
