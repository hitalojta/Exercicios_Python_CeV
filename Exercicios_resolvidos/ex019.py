#from random import choice
import random

a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
nomes = [a1, a2, a3, a4]
print(f'O(a) aluno(a) escolhido(a), aleatoriamente, foi o(a): {random.choice(nomes)}')
