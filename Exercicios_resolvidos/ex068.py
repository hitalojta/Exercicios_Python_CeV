from time import sleep
from random import randint
cont = 0
print('=-='*20)
print('\033[32mVAMOS JOGAR PAR OU ÍMPAR\033[m')
print('=-='*20)
sleep(1)
while True:
    num = int(input('\nDigite um valor inteiro positivo: '))
    while num < 0:
        print('\n\033[31mNúmero negativo não é válido!\033[m')
        sleep(1)
        num = int(input('\nDigite um valor inteiro positivo: '))
    pi = str(input('\nPar ou ímpar? [P/I]: ')).strip().lower()[0]
    while pi not in 'pi':
        print('\033[31mOpção inválida!\033[m')
        sleep(1)
        pi = str(input('Par ou ímpar? [P/I]: ')).strip().lower()[0]
    numpc = randint(0, 10)
    sleep(1)
    if (num + numpc) % 2 == 0:
        print(f'\nVocê jogou {num} e o computador {numpc}.'
              f'Total de {num + numpc} deu \033[36mPAR\033[m')
        PI = 'p'
    else:
        print(f'\nVocê jogou {num} e o computador {numpc}.'
              f'Total de {num + numpc} deu \033[36mÍMPAR\033[m')
        PI = 'i'
    sleep(1)
    if PI != pi:
        print('\n\033[31mVocê perdeu...\033[m\n')
        sleep(1)
        break
    print('\n\033[032mVocê venceu!\033[m Vamos jogar novamente...')
    cont += 1
    sleep(1)
print('=-='*20)
print(f'\n\033[33mGame Over! Você venceu {cont} vez(es).\033[m')
