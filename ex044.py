"""Elabore um programa que calcule o valor a ser pago por um produto,
 considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros"""
numParcela = 0
msg = ''
parcela = 0
print(('='*20) ,'Lojinha do Paulo', ('='*20))
produto = float(input('Digite o Preço do produto R$'))
condPagamento = int(input("""Qual é a condição de pagamento?
______________________________________________
[1] à vista dinheiro/cheque: 10% de desconto
[2] à vista no cartão: 5% de desconto
[3] em até 2x no cartão: preço formal
[4] 3x ou mais no cartão: 20% de juros
______________________________________________
DIGITE: """))
if condPagamento == 1:
    numParcela = produto * 0.9
    msg = '10% de desconto'
elif condPagamento == 2:
    numParcela = produto * 0.95
    msg = '5% de desconto'
elif condPagamento == 3:
    print('A compra será parcelada em 2x de R${:.2f} sem jurus'.format(produto / 2))
    numParcela = produto
    msg = 'Preço formal'
elif condPagamento == 4:
    parcela = int(input('Número de parcelas: '))
    numParcela = produto * 1.2
    msg = 'Juros de 20%'
    print('A compra será parcelada em {}x de R${:.2f}'.format(parcela, numParcela / parcela))
else:
    print('ERRO numero incorreto.')
if condPagamento <= 4:
    print('O produto custa R${:.2f}. Valor final R${:.2f}, {}'.format(produto, numParcela, msg))