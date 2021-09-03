"""
Faça um programa que calcule a soma entre todos os números
impares que são multiplos de 3 e que se encontram no intervalo
de 1 até 500.
"""

print('Soma de todos os números ímpares múltiplos de 3 no intervalo entre 1 e 500.')
s = 0
conta = 0
for c in range(1, 501, 2):  # aqui lista os impares
    if c % 3 == 0:  # aqui limita para os multiplos de 3
        s += c  # recebe ele mesmo + c
        conta += 1
print(f'\033[32mA soma de todos os {conta} valores solicitados é: {s}\033[m')
