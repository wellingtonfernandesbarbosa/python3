numeros = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
numeros[0].sort()
numeros[1].sort()
print('=' * 47)
print('Os números pares digitados foram: ', numeros[0])
print('Os números impares digitados foram: ', numeros[1])
