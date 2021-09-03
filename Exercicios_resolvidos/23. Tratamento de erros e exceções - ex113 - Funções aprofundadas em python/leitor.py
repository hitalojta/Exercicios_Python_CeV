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


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número real válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('Usuário preferiu não digitar um número.')
            return 0
        except Exception as erro:
            print(f'O erro encontrado foi {erro.__cause__}')
        else:
            return n

# nao consigo importar, dafuq ( pq não é __init__ ? )
