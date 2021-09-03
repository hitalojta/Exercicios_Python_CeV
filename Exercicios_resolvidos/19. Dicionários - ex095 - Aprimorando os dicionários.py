"""
Aprimore o desafio 93 para que ele funcione com varios jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento
de cada jogador
"""

jogadores = list()
temp = dict()
gols = list()
while True:
    sgols = 0
    temp['nome'] = str(input('Nome do jogador: ')).strip().title()
    part = int(input(f'Quantas partidas {temp["nome"]} jogou? '))
    for c in range(0, part):
        gol = int(input(f'Quantos gols na partida {c + 1}? '))
        gols.append(gol)
        sgols += gol
    temp['gols'] = gols[:]
    gols.clear()
    temp['total'] = sgols
    jogadores.append(temp.copy())
    temp.clear()
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('\033[31mOpção inválida!\033[m\nQuer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
    print('-' * 20)
print('-=' * 25)
print(f'{"cod":<4}{"nome"}{"gols":>15}{"total":>15}')
print('-' * 40)
for c in range(0, len(jogadores)):
    print(f'{c + 1:>3} {jogadores[c]["nome"]:<15}{str(jogadores[c]["gols"]):<15}{jogadores[c]["total"]}')
print('-' * 40)
while True:
    jog = int(input('Mostrar dados de qual jogador? (999 encerra): '))
    while jog < 1 or jog > len(jogadores) and jog != 999:
        print(f'\033[31mERRO!\033[m Não existe jogador com código {jog}! Tente novamente.')
        print('-' * 40)
        jog = int(input('Mostrar dados de qual jogador? (999 encerra): '))
    if jog == 999:
        break
    print('-' * 40)
    print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[jog - 1]["nome"]}:')
    for n, v in enumerate(jogadores[jog - 1]['gols']):
        print(f'No jogo {n + 1} fez {v} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')


# Fiz com busca pelo nome do jogador (33 linhas):
#
# lista = []
# while True:
#     dic = {"Nome":str(input('Qual o nome do jogador? ')).strip().capitalize(),
#            "Partidas":int(input('Quantas partidas jogadas? '))}
#
#     dic["Gols"] = sum([int(input(f'Quantos gols na partida {i}? ')) for i in range(1, dic["Partidas"]+1)])
#
#     dic["Média"] = float(dic["Gols"]/dic["Partidas"])
#
#     lista += [dic]
#
#     flag = str(input('\nContinuar? (S/N) ')).strip().lower()[0]
#     if flag == 'n':
#         break
#
# while True:
#     select = str(input('\nDeseja ver os dados de qual jogador? \n'
#                        '(Para sair, digite "sair")')).strip().capitalize()
#     if select == 'Sair':
#         break
#
#     i = 0
#     while lista[i]["Nome"] not in select:  ## Você 'obriga' o programa a loopar até achar a lista em que está o nome.
#         i += 1
#         if i == len(lista)-1 and lista[i]["Nome"] not in select:
#             print('Não há jogador com esse nome')
#             i = 0
#             select = str(input('\nDeseja ver os dados de qual jogador? \n'
#                                '(Para sair, digite "sair")')).strip().capitalize()
#
#     if lista[i]["Nome"] == select:
#         print('='*10, 'RESULTADO', '='*10)
#         print(f'Nome: {lista[i]["Nome"]}'
#               f'\nNúmero de partidas: {lista[i]["Partidas"]}'
#               f'\nNúmero total de gols: {lista[i]["Gols"]}'
#               f'\nMédia de gols por partida: {lista[i]["Média"]:.2f}')