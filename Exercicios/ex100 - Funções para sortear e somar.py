from random import randint
from time import sleep

numeros = list()


def titulo(msg):
    print('=' * (len(msg) + 37))
    print(f'{msg:^55}')
    print('=' * (len(msg) + 37))


def sorteio(lista):
    print('Os números sorteados foram: ', end='', flush=True)
    sleep(0.5)
    for n in range(0, 6):
        lista.append(randint(0, 99))
        print(lista[n], end=' ', flush=True)
        sleep(0.5)
    print()


def somapar(lista):
    s = 0
    print('Somando os números pares de ', end='', flush=True)
    sleep(0.5)
    for c in lista:
        print(c, end=' ', flush=True)
        if c % 2 == 0:
            s += c
            sleep(0.5)
    print(f'temos {s}.')


titulo('Sorteio de números')
sorteio(numeros)
somapar(numeros)
