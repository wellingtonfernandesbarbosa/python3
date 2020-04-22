from random import randint

numeros = list()


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(0, 50)
        print(n, end=' ', flush=True)
        lista.append(n)
    print('PRONTO!')


def pares(lista):
    somapar = 0
    print(f'Somando os valores pares de {numeros}, temos: ', end='')
    for c in lista:
        if c % 2 == 0:
            somapar += c
    print(somapar)


sorteia(numeros)
pares(numeros)
