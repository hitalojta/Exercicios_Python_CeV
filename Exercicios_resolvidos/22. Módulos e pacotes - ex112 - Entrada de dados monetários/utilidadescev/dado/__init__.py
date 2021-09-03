def leiadinheiro(msg):
    valido = False
    while not valido:
        m = str(input(msg)).strip().replace(',', '.')
        if m.isalpha() or m == '':
            print(f'\033[0;31mERRO: \"{m}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(m)
