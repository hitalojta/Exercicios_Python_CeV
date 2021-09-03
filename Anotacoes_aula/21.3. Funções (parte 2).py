#  Variáveis Globais e Locais
def teste(b):
    global a  # Colocando isso, chama o valor global de 'a'
    a = 8  # Nesse caso não mostra a global, pois é local!
    b += 4
    c = 2
    print(f'A variável \"a\" dentro vale {a}.')
    print(f'A variável \"b\" dentro vale {b}.')
    print(f'A variável \"c\" dentro vale {c}.')


#  Programa principal
a = 5
teste(a)
print(f'A variável \"a\" fora vale {a}.')
