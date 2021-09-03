print('Soma de todos os números ímpares múltiplos de 3 no intervalo entre 1 e 500.')
s = 0
conta = 0
for c in range(1, 501, 2):  #aqui lista os impares
    if c % 3 == 0:  #aqui limita para os multiplos de 3
        s += c  #recebe ele mesmo + c
        conta += 1
print(f'\033[32mA soma de todos os {conta} valores solicitados é: {s}\033[m')
