numeros = [0, 5, 7, 1, 8, 2]
numeros[3] = 9
numeros.append(10)
numeros.sort(reverse=True)
numeros.insert(2, 0)
if 3 in numeros:
    numeros.remove(3)
else:
    print('Não achei o valor 3')
print(numeros)
print(f'Essa lista tem {len(numeros)} elementos.')
