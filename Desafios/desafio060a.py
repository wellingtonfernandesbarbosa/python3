n = int(input('Digite um número para ver seu fatorial: '))
c = n
f = 1
print('Calculando {}! ='.format(n), end=' ')
for c in range(n, 1 - 1, -1):
    print('{}'.format(c), end=' ')
    print('x' if c > 1 else '=', end=' ')
    f *= c
    c -= 1
print('{}'.format(f))
