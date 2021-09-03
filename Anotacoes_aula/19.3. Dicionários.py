brasil = []
estado1 = {'uf': 'Rio de Janeiro',
           'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo',
           'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
print('-'*30)
estado = dict()
Brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: ')).strip().title()
    estado['sigla'] = str(input('Sigla do Estado: ')).strip().upper()
    Brasil.append(estado.copy())  # ASSIM INSERE DICIONARIO EM LISTA
print(Brasil)
print('-'*30)
for e in Brasil:
    print(e)
print('-'*30)
for e in Brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
print('-'*30)
for e in Brasil:
    for v in e.values():
        print(v, end=' ')
    print()