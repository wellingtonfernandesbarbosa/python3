def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    ficha = dict()
    ficha['Total'] = len(n)
    ficha['Maior'] = max(n)
    ficha['Menor'] = min(n)
    ficha['Média'] = sum(n)/len(n)
    if sit:
        if ficha['Média'] < 5:
            ficha['Situação'] = 'RUIM'
        elif 5 <= ficha['Média'] < 7:
            ficha['Situação'] = 'RAZOÁVEL'
        else:
            ficha['Situação'] = 'BOA'
    return ficha


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)
