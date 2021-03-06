"""
Faça um mini-sistema que utilize o interactive Help do python.
O usuário vai digitar o comando e o manual vai aparecer. Quando o
usuário digitar a palavra 'FIM', o programa se encerrará.
"""

from time import sleep

c = ('\033[m',          # 0 - Sem cores
     '\033[0;30;41m',   # 1 - vermelho
     '\033[0;30;42m',   # 2 - verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m',   # 4 - azul
     '\033[0;30;45m',   # 5 - roxo
     '\033[7;30m'       # 6 - branco
     )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(1)


def titulo(msg, cor=0):
    """
    Vamo testar saporra
    :return:
    """
    print(c[cor], end='')
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > ')).strip().lower()
    if comando == 'fim':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 2)
