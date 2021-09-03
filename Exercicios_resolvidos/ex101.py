# from datetime import date
#
#
# def voto(nasc):
#     global idade
#     idade = date.today().year - nasc
#     if idade < 16:
#         return 'NEGADO'
#     elif 16 <= idade < 18 or idade > 70:
#         return 'OPCIONAL'
#     else:
#         return 'OBRIGATÓRIO'
#
#
# print(f"O voto é {voto(int(input('Ano de Nascimento: ')))}", end='')
# print(f' para quem tem {idade} anos.')

# Guanabara


def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'


print(voto(int(input('Em que ano você nasceu? '))))
