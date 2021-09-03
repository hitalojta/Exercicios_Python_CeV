precobarato = contcaro = soma = 0
nomebarato = ''
print('-'*30)
print('{: ^30}'.format(' LOJA BARATEX '))
print('-'*30)
while True:
    nome = str(input('Digite o nome do produto: ')).strip()
    preco = float(input(f'Digite o preço do(a) {nome}: R$:'))
    if soma == 0 or preco < precobarato:
        precobarato = preco
        nomebarato = nome
    if preco > 1000:
        contcaro += 1
    soma += preco
    sair = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
    while sair not in 'sn':
        sair = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
    if sair == 'n':
        break
print('{:-^30}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R$:{soma:.2f}\n'
      f'Temos {contcaro} produto(s) custando mais de R$:1000.00\n'
      f'O produto mais barato foi o(a) {nomebarato} que custa R$:{precobarato:.2f}')
