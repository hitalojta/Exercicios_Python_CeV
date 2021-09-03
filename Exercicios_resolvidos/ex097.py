def escreva(texto):
    print('-' * (len(texto) + 4))
    print(f'  {texto}')
    print('-' * (len(texto) + 4))


escreva(str(input('Digite o texto: ')).strip())
