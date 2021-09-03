a1 = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite o valor da razão da P.A: '))
print('\n')

for n in range(1, 11):
    an = a1 + (n - 1)*r
    print(f'{an} ->', end=' ')
print('FIM')