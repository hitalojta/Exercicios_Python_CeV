from random import randint
from time import sleep
from termcolor import colored
cont = 0
vitoria = False
numpc = randint(0, 10)
print(colored('Sou seu computador...\n'
              'Acabei de pensar em um número inteiro entre 0 e 10.\n'
              'Será que você consegue adivinhar qual foi?', 'yellow'))
sleep(1)
while not vitoria:
    cont += 1
    num = int(input('Qual é seu palpite? '))
    sleep(1)
    if num == numpc:
        print(colored(f'\nParabéns! Acertou com {cont} tentativas!', 'green'))
        vitoria = True
    else:
        if num < numpc:
            print(colored('Pensei num número maior... Tente novamente.', 'red'))
            sleep(1)
        elif num > numpc:
            print(colored('Pensei num número menor... Tente novamente.', 'red'))
            sleep(1)

print('\n----- FIM DO JOGO -----')
