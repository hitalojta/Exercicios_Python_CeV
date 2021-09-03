# DICIONÁRIOS = {}

dados = {'nome': 'Pedro', 'idade': 25}  # nome / idade são as KEYS
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M'
del dados['idade']
print(dados)

filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'
         }

print(filme.values())
print(filme.keys())
print(filme.items())

for k, v in filme.items():
    print(f'O {k} é {v}.')
