def notas(*num, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: Uma ou mais notas dos alunos(aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: Dicionário com várias informações sobre a situação da turma
    """
    s = 0
    ficha = dict()
    for c in num:
        s += c
    ficha['Total'] = len(num)
    ficha['Maior'] = max(num)
    ficha['Menor'] = min(num)
    ficha['Média'] = s / len(num)
    if sit:
        if ficha['Média'] < 5:
            ficha['Situação'] = 'RUIM'
        elif 5 <= ficha['Média'] < 7:
            ficha['Situação'] = 'RAZOÁVEL'
        elif ficha['Média'] > 7:
            ficha['Situação'] = 'BOA'
    return ficha


resp = notas(5.5, 2.5, 10, 6.5, sit=True)
print(resp)
help(notas)
