# from random import randint
# numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
#      randint(1, 10), randint(1, 10))
# print('Os valores sorteados foram: ', end='')
# for n in numeros:
#     print(f'{n} ', end='')
# print(f'\nO maior valor foi {max(numeros)}.\nO menor {min(numeros)}.')


#  dos comentários do Youtube
from random import sample
a = tuple(sample(range(10), 5))
print(a)
print(f'O maior valor é {max(a)} e o menor é {min(a)}.')


#  fiz sem tuplas
# from random import randint
# maior = menor = 0
# print('Os valores sorteados foram: ', end='')
# for c in range(1, 6):
#     aleat = randint(0, 9)
#     print(f'{aleat}', end=' ')
#     if c == 1:
#         maior = aleat
#         menor = aleat
#     if aleat > maior:
#         maior = aleat
#     if aleat < menor:
#         menor = aleat
# print(f'\nO maior valor sorteado foi {maior}')
# print(f'O menor valor sorteado foi {menor}')