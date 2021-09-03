from time import sleep


def maior(*num):
    lista = list()
    print('-=' * 30)
    print('Analisando os valores passados...')
    if num[0] == 0 and len(num) == 1:
        print(f'Foram informados 0 valores ao todo.')
        print(f'O maior valor informado foi 0.')
    else:
        for p in num:
            lista.append(p)
            print(f'{p}', end=' ')
            sleep(0.5)
        print(f'Foram informados {len(lista)} valores ao todo.')
        print(f'O maior valor informado foi {max(lista)}')


#  Guanabara
def maior2(*num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior2(2, 9, 4, 5, 7, 1)
maior2(4, 7, 0)
maior2(1, 2)
maior2(6)
maior2()


