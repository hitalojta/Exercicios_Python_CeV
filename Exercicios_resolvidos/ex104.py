def leiaint(perg):
    num = input(perg)
    while not num.isnumeric():
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        num = input(perg)
    return int(num)


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
