sal = float(input('Qual o valor do salário?\n'))

if sal > 1250:
    print(f'Aumento salarial de 10%: {sal*0.1:.2f}\nValor final: {sal*1.1:.2f}')
else:
    print(f'Aumento salarial de 15%: {sal*0.15:.2f}\nValor final: {sal*1.15:.2f}')
