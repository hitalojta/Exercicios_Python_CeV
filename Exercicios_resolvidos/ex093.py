jogador = dict()
gols = list()
# sgols = 0
jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
part = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, part):
    gol = int(input(f'Quantos gols na partida {c}? '))
    gols.append(gol)
    # sgols += gol
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
# jogador['total'] = sgols
print('-=' * 25)
print(jogador)
print('-=' * 25)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 25)
print(f'O jogador {jogador["nome"]} jogou {part} partida(s).')
for c in range(0, part):
    print(f'\t=> Na partida {c}, fez {jogador["gols"][c]} gols.')
# print(f'Foi um total de {sgols} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
