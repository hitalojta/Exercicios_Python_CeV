def lin():
    print('-=' * 20)
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
s = s3 = 0
for c in range(0, 3):
    for c1 in range(0, 3):
        matriz[c][c1] = (int(input(f'Digite um valor para [{c}, {c1}]: ')))
        if matriz[c][c1] % 2 == 0:
            s += matriz[c][c1]
lin()
for c in range(0, 3):
    for c1 in range(0, 3):
        print(f'[{matriz[c][c1]:^5}]', end='')
    print()
lin()
print(f'A soma dos valores pares é: {s}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')
for p in matriz:
    s3 += p[2]
print(f'A soma dos valores da terceira coluna é: {s3}')
