"""Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preço, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular."""
produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Trasferidor', 4.20,
            'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
total = 0
x = '='*40
print(x)
print(f'{"MATERIAIS ESCOLARES":^40}')
print(x)
for p in range(0, len(produtos)):
    if p % 2 == 0:
        print(f'{produtos[p]:.<30}', end=' R$')
    else:
        print(f'{produtos[p]:.2f}')
        total += produtos[p]
print(x)
print('{:.<30} R${}'.format('TOTAL', total))
