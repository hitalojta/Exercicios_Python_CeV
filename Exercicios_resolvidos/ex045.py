from random import choice
from time import sleep
from emoji import emojize

opcoes = ['PEDRA', 'PAPEL', 'TESOURA']

print('-='*5, '\033[4;33mJO-KEN-PO\033[m', '=-'*5)
print(emojize('\n \033[33mVamos lá! Hora de jogar o clássico'
              ' pedra, papel ou tesoura! :smiley:\033[m\n'
              , use_aliases=True))
sleep(2)
mao = str(input('Digite qual das opções você irá jogar!\n\n'
                '\033[4;32mPEDRA\tPAPEL\tTESOURA\n\n'
                '\033[0;36mSua escolha é:\033[m ')).strip().upper()

sleep(1)
maopc = choice(opcoes)

if mao == 'PEDRA' or mao == 'TESOURA' or mao == 'PAPEL':
    print('\nCerto! Vamos lá! Preparem-se...\n')
    sleep(1)
    print('JO...\n')
    sleep(1)
    print('KEN...\n')
    sleep(1)
    print('PO!\n')
    sleep(0.5)
    print('Você: \033[1;36m{}\033[m <---- x ----> \033[1;35m{}\033[m :PC\n'
          ''.format(mao, maopc))
    sleep(1)
    if mao == 'PEDRA' and maopc == 'TESOURA' or \
            mao == 'PAPEL' and maopc == 'PEDRA' or \
            mao == 'TESOURA' and maopc == 'PAPEL':
        print(emojize(':confetti_ball: \032[33mVocê venceu! Parabéns!\033[m'
                      ' :confetti_ball:', use_aliases=True))
    elif mao == maopc:
        print(emojize('\033[33mEMPATE! :grimacing:\033[m\n'
                      'Tente novamente!', use_aliases=True))
    else:
        print(emojize('\033[31mVocê perdeu... :disappointed:\033[m\n'
                      'Tente novamente!', use_aliases=True))
else:
    print(emojize('\n\033[31mOps! Opção inválida! Assim não dá para '
                  'jogar... :neutral_face:\033[m\n'
                  'Verifique se escreveu corretamente e tente novamente.'
                  , use_aliases=True))
