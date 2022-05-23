"""Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais."""
palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'TRABALHO', 'MERCADO',
            'FUTURO', 'PROGRAMADOR', 'PRATICAR', 'ESTUDAR', 'GRATIS')
for palavra in palavras:
    print(f'\nNa palavra {palavra} temos as vogais: ', end=' ')
    for letra in palavra:
        if letra in 'AEIUO':
            print(letra.lower(), end=' ')

