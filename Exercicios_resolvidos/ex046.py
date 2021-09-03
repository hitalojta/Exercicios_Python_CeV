from time import sleep
from emoji import emojize

print('='*5, '\033[31mContagem regressiva para a queima dos fogos!\033[m', '='*5)
sleep(1)
for c in range(10, -1, -1):
    print(f'\t{c}')
    sleep(1)
print(emojize(':confetti_ball: :confetti_ball: \033[33mFeliz ano novo!\033[m :confetti_ball: :confetti_ball:', use_aliases=True))