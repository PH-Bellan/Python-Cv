""" Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite."""
velocidade = float(input('Qual é a velocidade do carro? '))
if velocidade > 80:
    print('\033[31mVocê foi multado!\033[m O valor da multa é de R${:.2f}. Você esta dirigindo a {}km/h'.format((velocidade - 80) *7, velocidade))
else:
    print('\033[36mVocê está dirigindo em uma velocidade segura.\033[m')
    
