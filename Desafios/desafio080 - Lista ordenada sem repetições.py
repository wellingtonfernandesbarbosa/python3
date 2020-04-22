lista = list()
n1 = int(input('Digite o 1º número: '))
lista.append(n1)
print('Adicionado ao final da lista...')
n2 = int(input('Digite o 2º número: '))
if n2 < lista[0]:
    lista.insert(0, n2)
    print('Adicionado na posição 0 da lista...')
else:
    lista.append(n2)
    print('Adicionado ao final da lista...')
n3 = int(input('Digite o 3º número: '))
if n3 < lista[0]:
    lista.insert(0, n3)
    print('Adicionado na posição 0 da lista...')
elif n3 < lista[1]:
    lista.insert(1, n3)
    print('Adicionado na posição 1 da lista...')
else:
    lista.append(n3)
    print('Adicionado ao final da lista...')
n4 = int(input('Digite o 4º número: '))
if n4 < lista[0]:
    lista.insert(0, n4)
    print('Adicionado na posição 0 da lista...')
elif n4 < lista[1]:
    lista.insert(1, n4)
    print('Adicionado na posição 1 da lista...')
elif n4 < lista[2]:
    lista.insert(2, n4)
    print('Adicionado na posição 2 da lista...')
else:
    lista.append(n4)
    print('Adicionado ao final da lista...')
n5 = int(input('Digite o 5º número: '))
if n5 < lista[0]:
    lista.insert(0, n5)
    print('Adicionado na posição 0 da lista...')
elif n5 < lista[1]:
    lista.insert(1, n5)
    print('Adicionado na posição 1 da lista...')
elif n5 < lista[2]:
    lista.insert(2, n5)
    print('Adicionado na posição 2 da lista...')
elif n5 < lista[3]:
    lista.insert(3, n5)
    print('Adicionado na posição 3 da lista...')
else:
    lista.append(n5)
    print('Adicionado ao final da lista...')
print('=' * 52)
print('Os valores digitados em ordem foram:', lista)

