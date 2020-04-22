cor = {'azulc': '\033[36m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'limpa': '\033[m'}
print('{}={}'.format(cor['azulc'], cor['limpa']) * 20)
print('10 TERMOS DE UMA PA'.format(cor['azul']))
print('{}='.format(cor['azulc']) * 20)
n = int(input('{}Primeiro termo: '.format(cor['amarelo'])))
r = int(input('Razão: '))
decimo = n + (10 - 1) * r
for c in range(n, decimo + 1, r):
    print('{}{}'.format(cor['azul'], n), end=' -> ')
    n += r
print('Acabou!')
