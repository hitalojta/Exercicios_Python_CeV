from random import randint
from time import sleep
from termcolor import colored

num = randint(0, 5)

num2 = int(input('Digite um número inteiro de 0 a 5:\n'))

print(colored('O computador está pensando... Hhhhmmmmmmmmmmmmmmmmm...', 'yellow'))

sleep(2) #Dá um tempo antes de proseguir.

print('O computador pensou no número: {}'.format(colored(num, 'blue')))

print(colored('Você acertou!!', 'green') if num == num2 else colored('Você errou...', 'red'))

