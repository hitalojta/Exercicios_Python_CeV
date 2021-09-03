"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados
aleatorios. Guarde esses resultados em um dicionario. No final,
coloque esse dicionario em ordem, sabendo que o vencedor tirou o maior
numero no dado.
"""

# from random import randint
# from time import sleep
#
# lista = []
# temp = {}
# print('\033[32mValores sorteados:\033[m')
# sleep(1)
# for c in range(1, 5):
#     temp['nome'] = f'jogador{c}'
#     temp['dado'] = randint(1, 6)
#     print(f'\tO {temp["nome"]} tirou {temp["dado"]}')
#     sleep(1)
#     if c == 1 or lista[c - 2]['dado'] >= temp['dado']:
#         lista.append(temp.copy())
#         temp.clear()
#     else:
#         pos = 0
#         while pos < len(lista):
#             if temp['dado'] >= lista[pos]['dado']:
#                 lista.insert(pos, temp.copy())
#                 break
#             pos += 1
# print('\033[33mRanking dos jogadores:\033[m')
# sleep(1)
# for c in range(1, 5):
#     print(f'\t{c}º lugar: {lista[c - 1]["nome"]} com {lista[c - 1]["dado"]}')
#     sleep(1)
#
# do Guanabara
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = []
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'  {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
