print('=' * 16)
print('Gerador de P.A')
print('=' * 16)
n = int(input('Primeiro termo: '))
r = int(input('Razão da P.A: '))
c = 1
while c <= 10:
    print('{} -> '.format(n), 'FIM' if c == 10 else '', end='')
    n += r
    c += 1
