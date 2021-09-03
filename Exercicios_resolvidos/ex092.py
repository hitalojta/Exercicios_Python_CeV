from datetime import date

dados = dict()
dados['nome'] = str(input('Nome: ')).strip().title()
dados['idade'] = date.today().year - int(input('Ano de Nascimento: '))
while dados['idade'] < 0:
    dados['idade'] = date.today().year - int(input('Ano de Nascimento: '))
dados['ctps'] = int(input('Nº da Carteira de Trabalho (0 não tem): '))
while dados['ctps'] < 0:
    dados['ctps'] = int(input('Nº da Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    while dados['contratacao'] < date.today().year - dados['idade']:
        dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$:'))
    while dados['salario'] < 0:
        dados['salario'] = float(input('Salário: R$:'))
    dados['aposentadoria'] = dados['idade'] + dados['contratacao'] + 35 - date.today().year
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
