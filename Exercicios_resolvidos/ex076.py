print('-'*30)
print(f"{' LISTAGEM DE PREÇOS ': ^30}")
print('-'*30)
lista = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9,
         'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
for c in range(0, len(lista), 2):
    print(f'{lista[c]:.<20}', f'R$:{lista[c + 1]:>6.2f}')
    # print(f'{lista[c]:.<15}{f"R$:{lista[c+1]:.2f}":.>15}')
print('-'*30)


'''dos comentários do YouTube'''
# for i in lista:
#     if type(i) is str:
#         print(f'{i:.<32}', end='')
#     else:
#         print(f'RS:{i:>5.2f}')
# print('-'*30)