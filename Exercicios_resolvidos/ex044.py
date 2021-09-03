print('{:=^40}'.format(' LOJAS ARAUJO '))

preco = float(input('\nDigite o valor do produto:\n'
                    '\033[33mR$:\033[m'))

cond = int(input('\nDigite o valor correspondente à condição de pagamento:\n'
                 '-> [ 1 ] À vista, dinheiro ou cheque\n'
                 '-> [ 2 ] À vista, cartão: 2\n'
                 '-> [ 3 ] Cartão, em até 2 parcelas: 3\n'
                 '-> [ 4 ] Cartão, em 3 parcelas ou mais: 4\n'
                 '\033[33mCONDIÇÃO:\033[m '))

if cond == 1:
    print(f'\nAplicado desconto de 10% no preço do produto: R$:{preco*0.9:.2f}')
elif cond == 2:
    print(f'\nAplicado desconto de 5% no preço do produto: R$:{preco*0.95:.2f}')
elif cond == 3:
    parcela = int(input('Digite se será em 1 ou 2 parcelas: '))
    if parcela == 1 or parcela == 2:
        vpar = preco / parcela
        print(f'\nPreço do produto se mantém: R$:{preco:.2f}\n'
              f'Parcelado em {parcela}x\nValor das parcelas: R$:{vpar:.2f}')
    else:
        print('\n\033[31mParcelamento inválido para essa condição de pagamento.\033[m')
elif cond == 4:
    parcela = int(input('Digite o número de parcelas: '))
    if parcela >= 3:
        vpar = (preco*1.2) / parcela
        print(f'\nParcelado em {parcela}x\nAplicado 20% de juros no preço do produto\nNovo valor do produto: R$:{preco*1.2:.2f}\n'
              f'Valor das parcelas: R$:{vpar:.2f}')
    else:
        print('\n\033[31mParcelamento inválido para essa condição de pagamento.\033[m')
else:
    print(f'\n\033[31mA condição {cond} não é válida. O programa será encerrado.\033[m')