from ex115.lib.interface import *


def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')  # read text QUERO LEITURA DE ARQUIVO TEXTO
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')  # write text create GRAVAÇÃO DE ARQUIVO TEXTO CRIANDO O ARQUIVO CASO NAO EXISTA
        a.close()
    except:
        print('\033[31mHouve um erro na criação do arquivo.\033[m')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mHouve um erro na leitura do arquivo!\033[m')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')  # Lê o arquivo e mostra no print
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')  # append text ADICIONAR TEXTO
    except:
        print('\033[31mHouve um erro na abertura do arquivo!\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31mHouve um erro na hora de escrever os dados!\033[m')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
