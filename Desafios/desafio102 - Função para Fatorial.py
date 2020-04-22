def fatorial(x, show=False):
    """
fatorial(x, show=False)
-> Calcula o Fatorial de um número.
:param x: O número a ser calculado
:param show: (opcional) Mostrar ou não a conta.
:return: O valor do Fatorial x
    """
    f = 1
    for c in range(x, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        f *= c
    print(f)


print('=' * 23)
fatorial(5, show=True)
fatorial(7)
help(fatorial)
