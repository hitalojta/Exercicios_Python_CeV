def mensagem(msg):
    print('-' * 30)
    print(f'{msg:^30}')
    print('-' * 30)


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


def contador(*num):  # o asterisco faz receber os parametros em tupla
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


def somatorio(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


mensagem("CURSO EM VIDEO")
mensagem("APRENDA PYTHON")
mensagem("GUSTAVO GUANABARA")
soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(b=5, a=9)
print('-=' * 30)
contador(4, 4, 7, 6, 2)
contador(2, 1, 7)
contador(8, 0)
print('-=' * 30)
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
print('-=' * 30)
somatorio(5, 2)
somatorio(2, 9, 4)
