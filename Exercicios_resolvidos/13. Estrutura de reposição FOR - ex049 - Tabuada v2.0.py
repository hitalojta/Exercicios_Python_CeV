"""
Refaça o desafio 9, mostrando a tabuada de um numero que
o usuario escolher, so que agora utilizando um laço FOR
"""

print('{:=^40}'.format(' TABUADA '))

num = int(input('Digite o número inteiro cuja tabuada será gerada: '))

print('\n{:-^40}'.format(f' TABUADA DO {num} '))

for c in range(1, 11):
    print('{: ^40}'.format(f' {num} x {c} = {c * num}'))

print('{:-^40}'.format(f' FIM '))