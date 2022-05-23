dias = int(input('Por quantos dias o carro foi alugado?: '))
km = float(input('Quantos kilometros rodados?: '))
valordia = 60.00
valorkm = 0.15
print('O carro foi alugado por {} dias e percorreu {} km. O total a pagar é R${:.2f}'.format(dias, km, valordia * dias + valorkm * km ))
