"""
Faça um programa que leia 5 valores numericos e guarde-os em
uma lista. No final, mostre qual foi o maior e o menor valor digitado
e as suas respectivas posições na lista
"""

maior = menor = 0
valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    if valores[c] >= maior:
        maior = valores[c]
    if valores[c] <= menor:
        menor = valores[c]
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for c1 in range(0, 5):
    if valores[c1] == maior:
        print(f'{c1}... ', end='')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for c2 in range(0, 5):
    if valores[c2] == menor:
        print(f'{c2}... ', end='')

# dos comentários do YouTube:
# lista = []
# posicao_maior = []
# posicao_menor = []
# for p in range(0, 5):
#     val = int(input(f'Digite um valor na posição {p}: '))
#     lista.append(val)
# for posicao, valores in enumerate(lista):
#     if valores == max(lista):
#         posicao_maior.append(posicao)
#     if valores == min(lista):
#         posicao_menor.append(posicao)
# print(f'Você digitou os valores {lista}')
# print(f'O maior valor da lista é {max(lista)}, nas posições {posicao_maior}')
# print(f'O menor valor da lista é {min(lista)}, nas posições {posicao_menor}')
