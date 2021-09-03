"""
Crie uma tupla preenchida com os 20 primeiros colocados da tabela
do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois
mostre:
a) Os 5 primeiros
b) Os ultimos 4 colocados
c) Times em ordem alfabetica
d) Em que posição está no time da Chapecoense
"""

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
