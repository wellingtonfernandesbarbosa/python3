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


def moeda(preço=0, moeda='R$'):
    return f'{moeda} {preço:.2f}'.replace('.', ',')
