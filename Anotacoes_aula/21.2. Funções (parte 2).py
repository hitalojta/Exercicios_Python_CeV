#  Parametros Opcionais
def somar(a=0, b=0, c=0):  # O '=' dá um valor inicial a variavel
    '''
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor.
    :param b: o segundo valor.
    :param c: o terceiro valor.
    :return: sem retorno
    Função criada pelo usuário!
    '''
    s = a + b + c
    print(f'A soma vale {s}.')


somar(3, 2, 5)
somar(8, 4)
somar(3)
somar()
somar(b=4, c=5)
help(somar)