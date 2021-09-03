"""
Melhore o desafio 61, perguntando para o usuário se ele quer mostrar
mais alguns termos. O programa encerra quando ele disser que quer
mostrar 0 termos.
"""

a1 = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite o valor da razão da P.A: '))

termos = int(input('\nDigite quantos termos você quer visualizar (Digite zero para encerrar): '))
while termos != 0:
    n = 1
    while n != termos + 1:
        an = a1 + (n - 1) * r
        print(f'{an} ->', end=' ')
        n += 1
    print('PAUSA')
    termos = int(input(('\nDigite quantos termos quer visualizar (Digite zero para encerrar): ')))
print('FIM')
print('\n\033[31m---- PROGRAMA ENCERRADO ----\033[m')
