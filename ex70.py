""" Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. """
total = cont1000 = cont = menor = 0
menornome = ''
while True:
    nomeproduto = input('NOME DO PRODUTO: ').strip().title()
    preco = float(input('PREÇO DO PRODUTO: R$ '))
    total += preco
    if cont == 0:
        menor = preco
        menornome = nomeproduto
    elif preco < menor:
        menor = preco
        menornome = nomeproduto
    cont += 1
    if preco > 1000:
        cont1000 += 1
    sair = input("Continuar? [S/N] ").strip()[0]
    if sair not in "Ss":
        break
print(f'Total gasto na compra: R${total:.2f}\nProdudos a cima de R$1000,00 Qtd.{cont1000}\n'
      f'O produto mais barato foi {menornome} custando R${menor:.2f}')
