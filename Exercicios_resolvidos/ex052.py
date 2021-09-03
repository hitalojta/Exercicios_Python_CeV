num = int(input('Digite um número inteiro positivo: '))

if num <= 2:
    print('\033[32mO número é primo!\033[m')
else:
    print('\n\033[33m1\033[m', end=' ')

    cont = 0
    for c in range(2, num):
        s = num % c
        if s != 0:
            cont += 1
            print(f'\033[31m{c}\033[m', end=' ')
        else:
            print(f'\033[33m{c}\033[m', end=' ')

    print(f'\033[33m{num}\033[m')

    div = 2 + (c - 1) - cont

    print(f'\nO número {num} foi divisível {div} vezes.')

    if cont == num - 2:
        print('Portanto, \033[32mO número é primo!\033[m')
    else:
        print('Portanto, \033[31mO número não é primo!\033[m')
