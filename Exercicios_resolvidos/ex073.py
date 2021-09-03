times = ('São Paulo', 'Atlético-MG', 'Internacional', 'Palmeiras',
         'Goiás', 'Botafogo', 'Grêmio', 'Chapecoense', 'Fortaleza',
         'Bragantino-SP', 'Vasco da Gama', 'Ceará SC', 'Bahia',
         'Atlético-GO', 'Sport Recife', 'Flamengo', 'Corinthians',
         'Santos', 'Fluminense', 'Coritiba')
print(f'Lista dos times em ordem de classificação: {times}')
print(f'5 primeiros colocados: {times[:5]}')
print('-=-' * 20)
print(f'4 últimos colocados: {times[-4:]}')
print('-=-' * 20)
print(f'Ordem alfabética: {sorted(times)}')
print('-=-' * 20)
print(f'Posição da Chapecoense: {1 + times.index("Chapecoense")}ª')
print('-=-' * 20)
