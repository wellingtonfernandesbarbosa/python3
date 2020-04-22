from random import randint
numeros = []
pares = []
impares = []
for c in range(0, 7):
    n = randint(0, 10)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
pares.sort()
impares.sort()
numeros.append(pares[:])
numeros.append(impares[:])
print('Os números pares digitados foram: ', numeros[0])
print('Os números impares digitados foram: ', numeros[1])
