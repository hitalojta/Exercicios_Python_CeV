"""
Crie um programa que leia dois valores e mostre um menu como o
ao lado da tela: Seu programa deverá realizar a operação solicitada
em cada caso.
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
"""

from time import sleep
menu = 0
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
while menu != 5:
    menu = int(input('\nDigite uma das opções:\n[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa\n-> '))
    while menu > 5 or menu < 1:
        menu = int(input('\n\033[31mOpção inválida!\033[m\n\nDigite uma das opções:\n[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa\n-> '))
    if menu == 1:
        soma = n1 + n2
        print(f'\nA soma de {n1:.2f} com {n2:.2f} é {soma}.')
        sleep(2)
    if menu == 2:
        mult = n1 * n2
        print(f'\nA multiplicação de {n1:.2f} por {n2:.2f} é {mult}.')
        sleep(2)
    if menu == 3:
        if n1 > n2:
            print(f'\nO número {n1} é maior do que o número {n2}.')
            sleep(2)
        elif n2 > n1:
            print(f'\nO número {n2} é maior que o número {n1}.')
            sleep(2)
        else:
            print(f'\n\033[33mO número {n1} é igual ao número {n2}.\033[m')
            sleep(2)
    if menu == 4:
        n1 = float(input('\nDigite o novo primeiro valor: '))
        n2 = float(input('Digite o novo segundo valor: '))
    if menu == 5:
        print('\n\033[35mO programa será encerrado. Até a próxima.\033[m')
