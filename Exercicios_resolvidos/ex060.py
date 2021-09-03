#  from math import factorial
num = int(input('Digite um número inteiro positivo: '))
print(f'\n{num}! = ', end='')

contfat = num
fat = num

#  USANDO WHILE
while contfat != 1:
    print(f'{contfat} x ', end='')
    contfat -= 1
    fat *= contfat
    if contfat == 1:
        #  Para ficar o 'x' certo poderia fazer print(' x ' if contfat > 1 else ' = ', end='')
        print(f'{contfat} = {fat}')
        print('\n\033[33m----- FIM DO PROGRAMA -----\033[m')

#  USANDO FOR
'''for c in range(num, 1, -1):
    print(f'{c} x ', end='')
    contfat = c - 1
    fat *= contfat

print(f'{contfat} = {fat}')
print('\n\033[33m----- FIM DO PROGRAMA -----\033[m')'''
