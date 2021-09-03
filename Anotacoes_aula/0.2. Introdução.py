nome = input('Qual o seu nome? ')
print('É um grande prazer te conhecer', nome)
#  python 2
print('É um grande prazer te conhecer %s' % (nome))
#  python 3
print('É um grande prazer te conhecer {}'.format(nome))
#  python 3.6+
print(f'É um grande prazer te conhecer {nome}')
