def aumentar(x, y):
    res = x + (x * y / 100)
    return res


def diminuir(x, y):
    res = x - (x * y / 100)
    return res


def dobro(x):
    res = x * 2
    return res


def metade(x):
    res = x / 2
    return res


def moeda(preco=0, tmoeda='R$'):
    return f'{tmoeda} {preco:.2f}'.replace('.', ',')


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
