from random import randint
from time import sleep
temp = []
jogos = []
print('-' * 40)
print(f'{"JOGA NA MESA SENA": ^40}')
print('-' * 40)
n = int(input('Quantos jogos quer que eu sorteie? '))
for c in range(1, n + 1):
    for c1 in range(1, 7):
        num = randint(1, 60)
        while num in temp:
            num = randint(1, 60)
        temp.append(num)
    jogos.append(sorted(temp[:]))
    temp.clear()
print('{:-^40}'.format(f' SORTEANDO {n} JOGOS '))
for n1, p in enumerate(jogos):
    print(f'Jogo {n1 + 1}: {p}')
    sleep(1)
print('{:-^40}'.format(' < BOA SORTE! > '))

# Do Youtube
# from random import sample
# from time import sleep
# jogos=list()
# n=int(input('Quantos jogos?: '))
# for c in range(n):
#   a=sorted(sample(range(1, 61), 6))
#   jogos.append(a[:])
#   print(f'Jogo {c+1}: {a}')
#   sleep(0.5)