"""
Faça um programa que tenha uma função chamada ficha(), que
receba dois parametros opcionais: o nome de um jogador e
quantos gols ele marcou. O programa deverá ser capaz de mostrar
a ficha do jogador, mesmo que algum dado não tenha sido
informado corretamente.
"""


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
