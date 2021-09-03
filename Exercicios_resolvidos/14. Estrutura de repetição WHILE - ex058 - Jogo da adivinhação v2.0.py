"""
Melhore o jogo do desafio 28 onde o computador vai "pensar" em
um numero entre 0 e 10. Só que agora o jogador vai tentar adivinhar
até acertar, mostrando no final quantos palpites foram necessarios
para vencer
"""

from random import randint
from time import sleep
from termcolor import colored

vitoria = False
contperda = 0
while not vitoria:
    num2 = int(input('Digite um número inteiro de 0 a 10: '))
    while num2 > 10 or num2 < 0:
        num2 = int(input('\nValor inválido. Digite novamente um número inteiro de 0 a 10:\n'))

    print(colored('\nO computador está pensando... Hhhhmmmmmmmmmmmmmmmmm...\n', 'yellow'))
    sleep(2)
    # Dá um tempo antes de proseguir.
    num = randint(0, 10)
    print('O computador pensou no número: {}\n'.format(colored(num, 'blue')))
    sleep(1)
    if num == num2:
        print(colored('Você acertou!!\n', 'green'))
        sleep(1)
        print(colored(f'Você perdeu {contperda} jogo(s) até a vitória.\n', 'yellow'))
        vitoria = True
        sleep(1)
    else:
        print(colored('Você perdeu... Tente novamente!\n', 'red'))
        contperda += 1
        sleep(1)

print(colored('--- Fim do Jogo ---', 'blue'))
