lista = []
for c in range(0, 3):
    for r in range(0, 3):
        lista.append(int(input(f'Digite um número para [{c}, {r}]: ')))
print('=' * 32)
print(f'[ {lista[0]} ] [ {lista[1]} ] [ {lista[2]} ]')
print(f'[ {lista[3]} ] [ {lista[4]} ] [ {lista[5]} ]')
print(f'[ {lista[6]} ] [ {lista[7]} ] [ {lista[8]} ]')
