def leia_dinheiro(msg):
    valido = False
    while not valido:
        entrada = input(msg).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'{entrada} não é um numero valido')
        else:
            valido = True
            return float(entrada)