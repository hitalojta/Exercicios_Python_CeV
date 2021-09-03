'''for c in range(1, 10):
    print(c)
print('fim')

c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')'''

n = 1
pares = impares = 0
while n != 0:  # n != 0 -> flag (condição de parada)
    n = int(input('Digite um valor ([0] encerra): '))
    if n != 0:
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1

print(f'Você digitou {pares} números pares e {impares} números ímpares.')
