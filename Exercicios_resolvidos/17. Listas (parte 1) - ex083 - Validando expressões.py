"""
Crie um programa onde o usuario digite uma expressao qualquer
que use parenteses. Seu aplicativo deverá analisar se a expressão
passada está com os parenteses abertos e fechados na ordem correta
"""

contesq = contdir = 0
exp = input('Digite a expressão: ').strip()
for c in range(0, len(exp)):
    if exp[c] == '(':
        contesq += 1
    elif exp[c] == ')':
        contdir += 1
if contesq == contdir:
    print('\033[32mSua expressão estã válida!\033[m')
else:
    print('\033[31mExpressão inválida!\033[m')

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('\033[32mSua expressão está válida!\033[m')
else:
    print('\033[31mExpressão inválida\033[m!')

# dos comentarios do youtube
# exp = str(input('Digite a expressão: '))
# if exp.count('(') == exp.count(')'):
#     print('Sua expressão é válida!!')
# else:
#     print('Sua expressão não é válida')
