from math import sqrt, floor
#import math
num = int(input('Digite um número: '))
#raiz = math.sqrt(num)
raiz = floor(sqrt(num))
print('A raiz de {} é igual a {:.2f}.'.format(num, (raiz)))

import random
num = random.random() #numero aleatorio de 0 a 1
print(num)

num2 = random.randint(1, 10) #numero inteiro aleatorio de 1 a 10
print(num2)

import emoji
print(emoji.emojize('Olá, mundo :thumbsup:', use_aliases=True))
