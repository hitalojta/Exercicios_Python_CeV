# Codigo ANSI (escape sequence)

''' \033[0;33;44m] # Para cor: \033[style_;text_;back_m] '''

print('\033[0;30;41mTeste\033[m\n') #no final é para limitar o background

print('\033[4;30;45mTeste\033[m\n')

print('\033[0;33;44mTeste\033[m\n')

print('\033[7;33;44mTeste\033[m\n') #o 7 inverte

a = 3
b = 5

print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m!!!')

nome = 'João'

print('Olá, {}{}{}. Muito prazer!'.format('\033[4;34m', nome, '\033[m'))

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'} #dicionário

print('Olá, {}{}{}. Muito prazer!'.format(cores['pretoebranco'], nome, cores['limpa']))
