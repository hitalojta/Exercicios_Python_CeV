s = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}o número:'))
    if num % 2 == 0:
        s += num
        cont += 1
print(f'\nForam informados {cont} números pares.\nSomatório: {s}')