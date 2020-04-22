from random import randint
from time import sleep
lista = []
numeros = []
print('=' * 37)
print(f'{" JOGOS DA MEGA SENA ":^37}')
print('=' * 37)
j = int(input('Quantos jogos quer que eu sorteie? '))
for c in range(0, j):
	for r in range(0, 6):
		n = randint(0, 60)
		if n in numeros:
			n = randint(0, 60)
		if n not in numeros:
			numeros.append(n)
	numeros.sort()
	lista.append(numeros[:])
	numeros.clear()
print(f'{f" SORTEANDO {j} JOGOS ":=^37}')
for c in range(0, j):
	print(f'{c + 1}º Jogo: ', lista[c])
	sleep(1)
print('=' * 37)
