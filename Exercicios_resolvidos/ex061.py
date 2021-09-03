a1 = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite o valor da razão da P.A: '))
print('\n')

n = 1
while n != 11:
    an = a1 + (n - 1) * r
    print(f'{an} ->', end=' ')
    n += 1
print('FIM')

#  com o for
'''for n in range(1, 11):
    an = a1 + (n - 1)*r
    print(f'{an} ->', end=' ')
print('FIM')'''

'''
# da video aula
termo = a1
n = 1
while n <= 10:
    print(f'{termo} -> ', end='')
    termo += r
    n += 1
print('FIM')'''