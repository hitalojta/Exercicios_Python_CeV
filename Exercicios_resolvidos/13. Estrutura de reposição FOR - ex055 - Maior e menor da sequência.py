"""
Faça um programa que leia o peso de cinco pessoas. No final,
mostre qual foi o maior e o menor peso lidos.
"""

pesolista = [0, 0, 0, 0, 0]

for c in range(1, 6):
    peso = float(input(f'Digite o valor, em quilos, da massa corpórea'
                       f' da pessoa número {c}: '))
    pesolista[(c-1)] = peso

print(f'\nA \033[1;33mMAIOR\033[m massa lida foi: {max(pesolista):.2f}\n'
      f'A \033[1;33mMENOR\033[m massa lida foi: {min(pesolista):.2f}')
