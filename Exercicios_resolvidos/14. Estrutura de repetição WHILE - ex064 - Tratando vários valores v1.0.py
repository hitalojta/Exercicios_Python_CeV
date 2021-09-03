"""
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que
é a condição de parada. No final, mostre quantos números foram
digitados e qual foi a soma entre eles (desconsiderando o flag)
"""

num = cont = soma = 0

num = int(input('Digite um número inteiro '
                    '(Digitar 999 encerra o programa): '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número inteiro '
                    '(Digitar 999 encerra o programa): '))

print(f'\nForam digitados: {cont} números.\nSomatório entre eles: {soma}.')

print('\n----- FIM DO PROGRAMA -----')