def linha():
    print('-'*25)


pessoas = {'nome': 'Gustavo',
           'sexo': 'M',
           'idade': 22}
print(pessoas['nome'])
linha()
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
linha()
print(pessoas.keys())
linha()
print(pessoas.values())
linha()
print(pessoas.items())
linha()
for k in pessoas.keys():
    print(k)
linha()
for v in pessoas.values():
    print(v)
linha()
for i in pessoas.items():
    print(i)
linha()
del pessoas['sexo']  # Deleta a chave sexo
for k, v in pessoas.items():
    print(f'{k} = {v}')
linha()
pessoas['sexo'] = 'M'  # Reinsere a chave sexo
pessoas['peso'] = 98.5  # insere nova chave
pessoas['nome'] = 'Leandro'  # insere novo valor à chave
for k, v in pessoas.items():
    print(f'{k} = {v}')
