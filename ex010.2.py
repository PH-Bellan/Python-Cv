print('Conversor de R$ para US$. dia 31/03/2022')
print('Converter R$ para US$ digite (1), converter US$ para R$ digite (2).')
c = int(input('Qual conversor vai utilizar?:'))
dolarcot = 4.75
if c == 1:
    real = float(input('Quantos reais você tem? R$'))
    print('R${:.2f} Reais brasileiros, equivalem a US${:.2f} Dólares americanos.'.format(real, real / dolarcot))
elif c == 2:
    dolar = float(input('Quantos dólares você tem? US$'))
    print('US${:.2f} Dólares americanos, equivalem a R${:.2f} Reais brasileiros.'.format(dolar, dolar * dolarcot))
else:
    print('somente (1) ou (2)')
    print('Converter R$ para US$ digite (1), converter US$ para R$ digite (2).')
    print('Reinicie o programa!')
2