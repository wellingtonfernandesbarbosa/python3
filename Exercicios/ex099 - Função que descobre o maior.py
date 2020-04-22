from random import randint
from time import sleep


def maior(lista):
    m = 0
    print('=' * (len(lista) * 4 + 27))
    print('Voce digitou os valores ', end='')
    for c in lista:
        print(c, end=' ', flush=True)
        if c == 0:
            m = c
        elif m < c:
            m = c
        sleep(0.5)
    print()
    print(f'O maior valor digitado foi: ', m)
    print('=' * (27 + len(lista) * 4))


numeros = [randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99)]
n = 0
maior(numeros)
while True:
    numeros.clear()
    while True:
        n = randint(0, 998)  # int(input('Digite um número: (999 para parar) '))
        t = randint(999, 1005)
        if t == 999:
            n = t
        if n == 999:
            break
        numeros.append(n)
    if len(numeros) > 0:
        maior(numeros)
    elif len(numeros) == 0:
        print('Não foi digitado nenhum valor válido.')
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('FINALIZANDO PROGRAMA', end='', flush=True)
sleep(0.5)
print('.', end='', flush=True)
sleep(0.5)
print('.', end='', flush=True)
sleep(0.5)
print('.', end='', flush=True)
