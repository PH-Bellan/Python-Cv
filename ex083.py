"""Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e
fechados na ordem correta."""
expressao = input('Digite uma expressão')
if expressao.find('(') > expressao.find(')') or expressao.count('(') != expressao.count(')')\
        or expressao[::-1].find(')') > expressao[::-1].find('('):
    print(f'A expressão [ {expressao} ] não é valida')
else:
    print(f'A expreção [{expressao}] é valida.')
