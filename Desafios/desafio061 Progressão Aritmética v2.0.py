n = int(input('Digite o primeiro termo: '))
r = int(input('Qual a razão? '))
c = 1
while c <= 10:
    print('{}'.format(n), end='')
    print(',' if c < 10 else '.', end=' ')
    n += r
    c += 1
