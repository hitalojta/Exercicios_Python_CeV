a1 = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A:'))

termo = int(input('Digite quantos termos quer mostrar: '))

n = 1
while n <= termo:
    while n <= termo:
        an = a1 + (n - 1) * r
        print(f'{an}', end=' -> ')
        n += 1
    print('PAUSA')
    termo += int(input('Quantos termos você quer mostrar a mais? '))

print(f'\nProgressão finalizada com {n - 1} termos mostrados.')


#  dos comentarios do youtube
'''p_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 10
while c > 0:
    print(p_termo, end=' ')
    p_termo += razao
    c -= 1
    if c == 0:
        c = int(input('\nAcrescentar mais números na sequência: '))'''