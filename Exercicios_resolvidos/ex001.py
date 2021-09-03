from time import sleep
from emoji import emojize
print('\033[36mPreparando...\033[m')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.')
sleep(1)
print('\033[33m{} \033[4;35mOlá, Mundo!\033[m \033[33m{}\033[m\n'.format('=-'*5, '-='*5))

cores = {'verm': '\033[31m',
         'lim': '\033[m',
         'verdN': '\033[1;32m'}

msg = '{0}É nozes{1} {2}:sunglasses:{1}!'.format(cores['verdN'],
                                             cores['lim'],
                                             cores['verm'])

print(emojize(msg, use_aliases=True))

