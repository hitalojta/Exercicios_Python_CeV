"""
Crie um programa onde o usuario possa digitar sete valores numericos
e cadastre-os em uma lista unica que mantenha separados os valores
pares e impares. No final, mostre os valores pares e impares em
ordem crescente
"""

num = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
print(f'Os valores digitados foram: {num}')
print(f'Os valores pares digitados foram: {sorted(num[0])}')
print(f'Os valores ímpares digitados foram: {sorted(num[1])}')
