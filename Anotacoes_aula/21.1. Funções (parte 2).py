#  Para receber informações de ajuda!
help(input)
print('-' * 30)
print(input.__doc__)
print('-' * 30)


def contador(i, f, p):  # logo após é inserida a docstring
    '''
    --> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    '''
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')


help(contador)
