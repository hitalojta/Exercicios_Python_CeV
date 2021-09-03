def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f  # Retorna de tudo, não só numeros.


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


n = int(input('Digite um numero: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}.')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2}, {f3}.')

if par(n):
    print(f'O número {n} é par!')
else:
    print(f'O número {n} é ímpar.')
