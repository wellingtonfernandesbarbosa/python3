lista = []
np = mv = tc = 0
print('=' * 43)
for c in range(0, 3):
    for r in range(0, 3):
        n = int(input(f'Digite um valor para [{c}, {r}]: '))
        if n % 2 == 0:
            np += n
        lista.append(n)
        if r == 2:
            tc += n
if mv == 0:
    mv = lista[3]
    if mv < lista[4]:
        mv = lista[4]
    if mv < lista[5]:
        mv = lista[5]
print('=' * 43)
print(f'A soma dos valores pares é {np}.')
print(f'A soma dos valores da terceira coluna é {tc}.')
print(f'O maior número da segunda linha é {mv}')
print('=' * 43)
