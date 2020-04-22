tot = 0
n = int(input('Digite um número: '))
for c in range(1, n + 1):
    if n % c == 0:
        tot += 1
        print('\033[33m', end=' ')
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\033[m')
if tot == 2:
    print('O número {} É PRIMO'.format(n))
else:
    print('O número {} NÃO É PRIMO.'.format(n))
