"""
A confederação nacional de natação precisa de um programa que
leia o ano de nascimento de um atleta e mostre sua categoria, de
acordo com a idade:
- até 9 anos: MIRIM            - até 19 anos: JUNIOR
- até 14 anos: INFANTIL         - até 25 anos: SENIOR
                                - acima: MASTER
"""

from datetime import date
ano = int(input('Digite o ano de nascimento do atleta:\n'))
anohj = date.today().year
idade = anohj - ano

if idade <= 9:
    print(f'O atleta tem {idade} anos.\n'
          f'\nPortanto, sua categoria é \033[4;36mMIRIM\033[m.')
elif 9 < idade <= 14:
    print(f'O atleta tem {idade} anos.\n'
          f'\nPortanto, sua categoria é \033[4;36mINFANTIL\033[m.')
elif 14 < idade <= 19:
    print(f'O atleta tem {idade} anos.\n'
          f'\nPortanto, sua categoria é \033[4;36mJÚNIOR\033[m.')
elif 19 < idade <= 25:
    print(f'O atleta tem {idade} anos.\n'
          f'\nPortanto, sua categoria é \033[4;36mSÊNIOR\033[m.')
else:
    print(f'O atleta tem {idade} anos.\n'
          f'\nPortanto, sua categoria é \033[4;36mMASTER\033[m.')
