"""
Faça um programa que leia um ano qualquer e mostre
se ele é BISSEXTO
"""

from datetime import date

ano = int(input('Digite o ano a ser avaliado (Digite zero para o atual):\n'))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} NÃO é bissexto!')



'''checa = ano % 4
if ano < 100:
    print('Ano bissexto!' if checa == 0 else 'Ano não bissexto.')
else:
    if checa != 0:
        print('Ano não bissexto.')
    else:
        if ano % 100 != 0:
            print('Ano bissexto!')
        else:
            if ano % 400 == 0:
                print('Ano bissexto!')
            else:
                print('Ano não bissexto.')'''