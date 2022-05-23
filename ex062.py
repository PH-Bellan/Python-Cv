"""Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos."""
print('Gerador de PA')
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
PA = primeiro
termo = 0
total = 0
mais = 10
while mais != 0:
    total += mais
    while termo < total:
        print(PA, end=' ')
        PA += razao
        termo += 1
    mais = int(input('\nQuantos termos Você quer mostrar mais?: '))
print('Finalizado...')
print('No total foram mostrados ', total, ' termos.')


