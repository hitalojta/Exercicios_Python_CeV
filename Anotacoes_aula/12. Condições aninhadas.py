nome = str(input('Digite seu nome: '))
if nome == 'Gustavo':
    print(f'Que nome coisado...')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print('Que nome comum...')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Olá, garbosa moçoila...')
else:
    print('Seu nome é bem méh...')
print(f'Firmeza, \033[4;34m{nome}\033[m')
