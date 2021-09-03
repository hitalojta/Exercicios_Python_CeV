def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um valor inteiro válido!\033[m')
            continue  # Reseta o while (redundante?)
        except KeyboardInterrupt:
            print('Usuário preferiu não digitar um número.')
            return 0
        except Exception as erro:
            print(f'O erro encontrado foi {erro.__cause__}')
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c} - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[32mSua opção: \033[m')
    return opc
