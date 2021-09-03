"""
Faça um programa que tenha uma função chamada contador(), que
receba três parametros: inicio, fim e passo. Seu programa tem
que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""

from time import sleep


def contador(inicio, fim, passo):
    print('-=' * 30)
    if passo == 0:
        passo = 1
    passo = abs(passo)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio > fim:
        passo = -passo
        fim -= 1
    else:
        fim += 1
    for c in range(inicio, fim, passo):
        print(f'{c}', end=' ')
        sleep(0.5)
    print('FIM!')
    sleep(1)


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
