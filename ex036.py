""" Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
 Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
 A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado."""
valcasa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o salário do comprador: R$'))
anosapagar = int(input('Digite quantos anos a pagar: '))
prestacao = valcasa / (anosapagar * 12)
print('O emprestimo terá que ser pago em {} anos no valor mensal de R${:.2f}.'.format(anosapagar, prestacao,),end='')
if prestacao > salario * 0.3:
    print(' O emprestimo foi NEGADO')
else:
    print(' O emprestimo foi APROVADO!!')




