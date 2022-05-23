""": Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time do Corinthias."""
times = ('Santos', 'Atlético-MG', 'Corinthias', 'Cuiabá', 'Internacional',
         'Avaí', 'Bragantino', 'Palmeiras', 'Flamengo', 'Curitiba',
         'São Paulo', 'Botafogo', 'Fluminense', 'América-MG', 'Ceará SC',
         'Athletico-PR', 'Atlético-GO', 'Goías', 'Juventude', 'Fortaleza')
print('Brasileirão 2022 dia 26/04/2022')
print(times)
print(f'Os 5 primeiros colocados são {times[:5]}\n'
      f'Os 4 útimos colacados são {times[-4:]}\n'
      f'Times em ordem alfabética {sorted(times)}\n'
      f'O Corinthias está na {times.index("Corinthias")}º posição.')
