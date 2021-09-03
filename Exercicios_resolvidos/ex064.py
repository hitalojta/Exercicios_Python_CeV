num = cont = soma = 0

num = int(input('Digite um número inteiro '
                    '(Digitar 999 encerra o programa): '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número inteiro '
                    '(Digitar 999 encerra o programa): '))

print(f'\nForam digitados: {cont} números.\nSomatório entre eles: {soma}.')

print('\n----- FIM DO PROGRAMA -----')