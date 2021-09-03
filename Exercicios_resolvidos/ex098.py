from time import sleep


def contador(inicio, fim, passo):
    print('-=' * 30)
    if passo == 0:
        passo = 1
    passo = abs(passo)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio > fim:
        passo = -passo
        fim -= 1
    else:
        fim += 1
    for c in range(inicio, fim, passo):
        print(f'{c}', end=' ')
        sleep(0.5)
    print('FIM!')
    sleep(1)


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
