
cont = 0
total = 0
n = int(input('Digite um numero ou digite 999 para para: '))
while n != 999:
    cont += 1
    total += n
    n = int(input('Digite um numero ou digite 999 para para: '))
print('Foram digitados {} números e a soma de todos eles é {}'.format(cont, total))
