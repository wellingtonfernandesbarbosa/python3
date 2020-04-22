print('=' * 33)
print('Gerador de Progressão Aritimética')
print('=' * 33)
n = int(input('Primeiro termo: '))
r = int(input('Razão da P.A: '))
t = 0
c = 1
m = 10
while m != 0:
    t = t + m
    while c <= t:
        print('{} -> '.format(n), end='')
        n += r
        c += 1
    print('PAUSA')
    m = int(input('Quantos termos você quer mostrara mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(t))
