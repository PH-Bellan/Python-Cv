""" Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
"""
frase = input('Digite uma frase: ').strip().upper()
cont = 1
SPLIT = frase.split()
junta = ''.join(SPLIT)
salva = ''
for a in range(len(junta)):
    salva += junta[len(junta) - cont]
    cont += 1
print('A frase {} escrita de trás para frente é {}'.format(frase, (salva.strip())))
if junta == salva.strip():
    print('A frase {} é uma frase PÁLIDROMA'.format(frase))
else:
    print('A frase {} NÃO é uma frase PÁLIDROMA'.format(frase))
