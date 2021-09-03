lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print('-='*20)
print(f'Os valores digitados em ordem foram {lista}')


# dos comentários do YouTube
# lista = []
# for c in range(5):
#     n = int(input('Número: '))
#     if c == 0 or n > lista[-1]:
#         lista.append(n)
#         print('O número foi adicionado no final da lista.')
#     else:
#         for i in range(5):
#             if n <= lista[i]:
#                 lista.insert(i,n)
#                 print(f'O número foi adicionado na posição {i}.')
#                 break
# print(lista)
