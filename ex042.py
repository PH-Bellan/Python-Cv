"""Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes"""
tipo = ''
resultado = ''
print('Informe 3 retas e descubra se é possivel formar um triangilo e que tipo de triangulo ele é.')
a = float(input('Informe um lado do triangulo:'))
b = float(input('Informe outro lado do triangulo: '))
c = float(input('Informe o ultimo lado do triangulo: '))
if (a + b) > c and (a + c) > b and (c + b) > a:
    print('É POSSIVEL formar um triangulo ', end='')
    if a == b == c:
        print('EQUILÁTERO')
    elif a == b != c or a == c != b or b == c != a:
        print('ISÓSCELES')
    elif a != b != c != a:
        print('ESCALENO')
else:
    print('NÃO É POSSIVEL formar um triangulo')


