""": Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo,
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos."""
# variaveis
somatoria = 0
m_velho = 0
f_jovem = 0
nomemaisvelho = ''
x = '=' * 40

for p in range(1, 5):
    print(x)
    print('{:^40}'.format('{}º PESSOA'.format(p)))
    print(x)
    nome = input('Digite o nome da pessoa: ').strip().title()
    idade = int(input('Digite a idade do/a {} '.format(nome)))
    sexo = input('Digite o sexo do/a {} (m/f) '.format(nome)).strip().lower()
    somatoria += idade
    if sexo != 'm' and sexo != 'f':
        print('ERRO sexo invalido')
    if sexo == 'f' and idade < 20:
        f_jovem += 1
    if sexo == 'm':
        if idade > m_velho:
            m_velho = idade
            nomemaisvelho = nome
print(x)
print('A média de idade do grupo é de {:.0f} anos'.format(somatoria / 4))
print('{} mulher/es menor/es que 20 anos'.format(f_jovem))
print('O homem mais velho tem {} anos e se chama {}'.format(m_velho, nomemaisvelho))
print(x)
