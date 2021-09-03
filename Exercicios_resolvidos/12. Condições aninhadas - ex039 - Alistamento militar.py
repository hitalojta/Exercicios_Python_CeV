"""
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora de se alistar ou se já passou do tempo de alistamento.
Seu programa também deverá mostrar o tempo que falta ou que
passou do prazo.
"""

from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
anohj = date.today().year
idade = anohj - ano
if idade < 18:
    print(f'\nVocê faz {idade} anos nesse ano. Ainda irá alistar-se.\n\n'
          f'\033[32mFaltam {18 - idade} anos para isso.\033[m')
elif idade > 18:
    print(f'\nVocê faz {idade} anos nesse ano.\n\n'
          f'\033[31mJá passou {idade - 18} anos do prazo!\033[m')
else:
    print(f'\nVocê faz {idade} anos nesse ano.\n\n'
          f'\033[33mÉ hora de se alistar!\033[m')
