"""
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores
"""

from datetime import date

cont = 0
for c in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da pessoa número {c}: '))
    anohj = date.today().year
    if anohj - ano < 21:
        cont += 1

print(f'\nDas 7 pessoas:\n{cont} são menores de idade.\n{7 - cont} são maiores de idade.')
