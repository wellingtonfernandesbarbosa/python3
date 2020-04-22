from time import sleep
n = 0


def maior(lst):
    print('=' * 50)
    print('Analizando os valores informados...')
    m = lst[0]
    for c in lst:
        print(c, end=' ', flush=True)
        sleep(0.5)
        if m < c:
            m = c
    print(f'Foram informados {len(lst)} valores ao todo.')
    print(f'O maior valor informado foi {m}')
    print('=' * 50)


print('=' * 50)
lista = list()
while n != 999:
    while True:
        n = int(input('Digite um número: (999 para parar) '))
        if n == 999:
            break
        lista.append(n)
    if len(lista) > 0:
        maior(lista)
    if n == 999:
        break
n = 0
lista1 = list()
while n != 999:
    while True:
        n = int(input('Digite um número: (999 para parar) '))
        if n == 999:
            break
        lista1.append(n)
    if len(lista1) > 0:
        maior(lista1)
    if n == 999:
        break
n = 0
lista2 = list()
while n != 999:
    while True:
        n = int(input('Digite um número: (999 para parar) '))
        if n == 999:
            break
        lista2.append(n)
    if len(lista2) > 0:
        maior(lista2)
    if n == 999:
        break
n = 0
lista3 = list()
while True:
    while True:
        n = int(input('Digite um número: (999 para parar) '))
        if n == 999:
            break
        lista3.append(n)
    if len(lista3) > 0:
        maior(lista3)
    if n == 999:
        break
