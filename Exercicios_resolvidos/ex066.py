cont = s = 0
while True:
    n = int(input('Digite um número (999 encerra): '))
    if n == 999:
        break
        #  Quebra o while e sai dele instantaneamente.
    s += n
    cont += 1
print(f'\nForam {cont} números digitados de soma {s}.')