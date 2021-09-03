num = list(range(0, 7, 2))
print(num)

num = [2, 5, 9, 1]
print(num)

num[2] = 3
print(num)

num.append(7)
print(num)

num.sort()
print(num)

num.sort(reverse=True)
print(num)

print(f'Essa lista possui {len(num)} elementos.')

num.insert(2, 0)
print(num)

num.pop()
print(num)

num.pop(2)
print(num)

num.append(5)
print(num)

num.remove(5)
print(num)

if 4 in num:  # isso para evitar dar erro
    num.remove(4)
print(num)

print('-------------------')

valores = list()  # Ou então: valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)

for v in valores:
    print(f'{v}...', end='')

# for cont in range(0, 5):
#     valores.append(int(input('Digite um valor a ser inserido: ')))

for c, n in enumerate(valores):
    print(f'\nNa posição {c} encontrei o valor {n}!')
print('Fim da lista')

#  ---------------------

a = [2, 3, 4, 7]
# b = a  # AS LISTAS FICAM CONECTADAS! O que fizer em uma, altera a outra
b = a[:]  # RECEBE UMA COPIA DOS ELEMENTOS! Listas independentes
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
