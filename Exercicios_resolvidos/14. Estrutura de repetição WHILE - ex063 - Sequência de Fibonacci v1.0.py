"""
Escreva um programa que leia um número "N" inteiro qualquer e
mostre na tela os "N" primeiros elementos de uma sequencia de
Fibonacci.
"""

print('\033[33m----- SEQUENCIA DE FIBONNACI -----\033[m\n')

n = int(input('Digite quantos elementos serão mostrados: '))
print('')
fibantes = 0
fibdepois = 1
fib = 0
#  no while já começa com 2 termos
c = 2
if n == 1:
    print('0')
elif n == 2:
    print('0 -> 1')
else:
    print('0 -> 1', end='')
    while c != n:
        fib = fibantes + fibdepois
        print(f' -> {fib}', end='')
        fibantes = fibdepois
        fibdepois = fib
        c += 1
print('\n\n\033[33m----- FIM DO PROGRAMA -----\033[m')

#  dos comentários do youtube
'''Nant = 1
Fibonacci = 0

n = int(input('Digite um número:(Este vai ser o nº de elementos da sequência) '))

while n != 0:
    print('{}'.format(Fibonacci), end=' → ')
    Fibonacci = Fibonacci + Nant
    Nant = Fibonacci - Nant
    n -= 1
print('FIM')'''