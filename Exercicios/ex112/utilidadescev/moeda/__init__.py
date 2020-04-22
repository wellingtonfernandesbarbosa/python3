def aumentar(preco, taxa, formatar=False):
    """

    :param preco:
    :param taxa:
    :param formatar:
    :return:
    """
    res = preco + (preco * taxa / 100)
    return res if formatar is False else moeda(res)


def diminuir(preco, desconto, formatar=False):
    """

    :param preco:
    :param desconto:
    :param formatar:
    :return:
    """
    res = preco - (preco * desconto / 100)
    return res if not formatar else moeda(res)


def dobro(preco, formatar=False):
    """

    :param preco:
    :param formatar:
    :return:
    """
    res = preco * 2
    if formatar:
        return moeda(res)
    return res


def metade(preco, formatar=False):
    """

    :param preco:
    :param formatar:
    :return:
    """
    res = preco / 2
    if formatar:
        return moeda(res)
    return res


# noinspection NonAsciiCharacters
def moeda(preço=0, tipo='R$'):
    """

    :param preço:
    :param tipo:
    :return:
    """
    return f'{tipo} {preço:.2f}'.replace('.', ',')


def resumo(x, y, z):
    d = {'Preço analisado: ': x,
         'Dobro do valor: ': x * 2,
         'Metade do preço: ': x / 2,
         f'{y}% de aumento: ': x + (x * y / 100),
         f'{z}% de redução: ': x - (x * z / 100)
         }
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    for k, v in d.items():
        print(f'{k:<20}R$', end='')
        print(f'{v:>8.2f}'.replace('.', ','))
    print('-' * 30)


def resumo1(preco, taxa=0, desconto=0):
    """

    :param preco:
    :param taxa:
    :param desconto:
    :return:
    """
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxa}% de aumento: \t{aumentar(preco, taxa, True)}')
    print(f'{desconto}% de deconto: \t{diminuir(preco, desconto, True)}')
    print('-' * 30)
