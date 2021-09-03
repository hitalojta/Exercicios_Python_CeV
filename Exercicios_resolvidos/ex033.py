n1 = float(input('Digite o primeiro número:\n'))
n2 = float(input('Digite o segundo número:\n'))
n3 = float(input('Digite o terceiro número:\n'))

maior = n1
if n2 >= n1 and n2 >= n3:
    maior = n2
if n3 >= n1 and n3 >= n2:
    maior = n3

menor = n1
if n2 <= n1 and n2 <= n3:
    menor = n2
if n3 <= n1 and n3 <= n2:
    menor = n3

print(f'Maior valor: {maior}\nMenor valor: {menor}')


#simplificado
#list = a, b, c = input('').split(' ')
#print('O valor máximo é {} e o valor mínimo é {}'.format(max(list), min(list)))


'''if n1 >= n2 >= n3:
    print(f'Maior: {n1}\nMenor: {n3}')
else:
    if n1 >= n3 >= n2:
        print(f'Maior: {n1}\nMenor: {n2}')
    else:
        if n2 >= n1 >= n3:
            print(f'Maior: {n2}\nMenor: {n3}')
        else:
            if n2 >= n3 >= n1:
                print(f'Maior: {n2}\nMenor: {n1}')
            else:
                if n3 >= n1 >= n2:
                    print(f'Maior: {n3}\nMenor: {n2}')
                else:
                    if n3 >= n2 >= n1:
                        print(f'Maior: {n3}\nMenor: {n1}')
                    else:
                        print('Tem algo errado com o algoritmo...')
'''