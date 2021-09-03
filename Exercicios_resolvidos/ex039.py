from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
anohj = date.today().year
idade = anohj - ano
if idade < 18:
    print(f'\nVocê faz {idade} anos nesse ano. Ainda irá alistar-se.\n\n'
          f'\033[32mFaltam {18 - idade} anos para isso.\033[m')
elif idade > 18:
    print(f'\nVocê faz {idade} anos nesse ano.\n\n'
          f'\033[31mJá passou {idade - 18} anos do prazo!\033[m')
else:
    print(f'\nVocê faz {idade} anos nesse ano.\n\n'
          f'\033[33mÉ hora de se alistar!\033[m')
