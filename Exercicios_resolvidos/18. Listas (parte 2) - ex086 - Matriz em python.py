"""
Crie um programa que crie uma matriz de dimensao 3x3 e preencha
com valores lidos pelo teclado. No final, mostre a matriz na tela,
com a formatação correta.
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for c in range(0, 3):
    for c1 in range(0, 3):
        matriz[c][c1] = (int(input(f'Digite um valor para [{c}, {c1}]: ')))
print('-='*30)
for c in range(0, 3):
    for c1 in range(0, 3):
        print(f'[{matriz[c][c1]:^5}]', end='')
    print()
