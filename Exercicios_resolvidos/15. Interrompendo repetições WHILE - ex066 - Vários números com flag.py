"""
Cire um programa que leia vários números inteiros pelo teclado. O
programa só vai parar quando o usuário digitar o valor 999, que é a
condição de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre eles (desconsiderando o flag).
"""

cont = s = 0
while True:
    n = int(input('Digite um número (999 encerra): '))
    if n == 999:
        break
        #  Quebra o while e sai dele instantaneamente.
    s += n
    cont += 1
print(f'\nForam {cont} números digitados de soma {s}.')