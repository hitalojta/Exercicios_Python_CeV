"""
Faça um programa que tenha uma função notas() que pode receber
várias notas de alunos e vai retornar um dicionário com as seguintes
informações:
- quantidade de notas
- a maior nota
- a menor nota
- a media da turma
- a situação (opcional)
- Adicione tambem as docstrings
"""


def notas(*nota, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param nota: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação do aluno.
    '''
    dic = dict()
    dic['total'] = len(nota)
    dic['maior'] = max(nota)
    dic['menor'] = min(nota)
    dic['média'] = sum(nota) / len(nota)
    if sit:
        if dic['média'] >= 7:
            dic['situação'] = 'BOA'
        elif 7 > dic['média'] >= 5:
            dic['situação'] = 'RAZOÁVEL'
        else:
            dic['situação'] = 'RUIM'
    return dic


#  Programa principal
resp = notas(5, 5, 4, 6, 8, 12, 4, 9, sit=True)
print(resp)
help(notas)
