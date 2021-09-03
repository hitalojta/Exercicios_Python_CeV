"""
Reescreva a função leiaint() que fizemos no desafio 104, incluindo
agora a possibilidade da digitação de um numero de tipo invalido.
Aproveite e crie tambem uma função leiafloat() com a mesma
funcionalidade.
"""

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


n = leiaint('Digite um número inteiro: ')
n2 = leiafloat('Digite um número real: ')
print(f'Você digitou o número inteiro {n} e o número real {n2}')
