matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for c in range(0, 3):
    for c1 in range(0, 3):
        matriz[c][c1] = (int(input(f'Digite um valor para [{c}, {c1}]: ')))
print('-='*30)
for c in range(0, 3):
    for c1 in range(0, 3):
        print(f'[{matriz[c][c1]:^5}]', end='')
    print()
