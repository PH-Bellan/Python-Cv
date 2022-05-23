""" Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
 calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida"""
peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
imc = peso / (altura **2)
msg = ''
if imc < 18.5:
    msg = 'Abaixo do peso'
elif imc <= 25:
    msg = 'Peso ideal'
elif imc <= 30:
    msg = 'Sobrepeso'
elif imc <= 40:
    msg = 'Obesidade'
elif imc > 40:
    msg = 'Obesidade Mórbida'
print('O seu peso é {}kg e altura {}m.'.format(peso, altura))
print('O seu indice de massa corporea é de {:.1f}. ou seja, {}'.format(imc, msg))
