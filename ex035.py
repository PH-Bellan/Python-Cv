"""Desenvolva um programa que leia o comprimento de três retas
 e diga ao usuário se elas podem ou não formar um triângulo."""
print('Informe 3 retas e descubra se é possível formar um triângulo')
unidade = input('Informe a unidade: ').strip()
a = float(input('Digite o comprimeto de uma reta: '))
b = float(input('Digite o comprimeto de outra reta: '))
c = float(input('Digite o comprimento da ultima reta: '))
if (a + b) > c and (a + c) > b and (c + b) > a:
    print('Com as retas {}{}, {}{} e {}{}; é possivel formar um triangulo!!!'.format(a, unidade, b, unidade, c, unidade))
else:
    print('Com as retas {}{}, {}{} e {}{}; não é possivel formar um triangulo.'.format(a, unidade, b, unidade, c, unidade))
