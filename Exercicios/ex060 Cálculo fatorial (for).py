n = int(input('Digite um número para calcular seu fatorial: '))
f = 1
print('Calculando {}! = '.format(n), end='')
for n in range(n, 0, -1):
    print('{}'.format(n), 'x ' if n > 1 else '=', end='')
    f *= n
    n -= 1
print(' {}'.format(f))
