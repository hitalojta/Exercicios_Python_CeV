def ficha(nome="<desconhecido>", gols=0):
    print('-' * 20)
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


n = str(input('Nome: ')).strip().title()
g = str(input('Nº de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    ficha(gols=g)
else:
    ficha(n, g)
