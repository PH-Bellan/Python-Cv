""" Crie um programa que leia duas notas de um aluno e calcule sua média,
 mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO"""
nota1 = float(input('Digite a nota p1 do aluno: '))
nota2 = float(input('Digite a nota p2 do aluno: '))
media = (nota1 + nota2) / 2
print('A media do aluno nesse bimestre foi {}.'.format(media))
if media > 7:
    print('Aluno APROVADO!!!')
elif media < 5:
    print('Aluno REPROVADO')
elif media >= 5 or media <= 6.9:
    print('Aluno de RECUPERAÇÃO.')

