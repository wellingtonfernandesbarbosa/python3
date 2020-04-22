print('{}-=-'.format('\033[34m') * 9)
print('   ANALIZADOR DE NÚMEROS')
print('-=-' * 9)
n = int(input('{}Digite um número: '.format('\033[33m')))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('{}Analizando o número {}.'.format('\033[36m', n))
print('Unidade: {}'.format(u))
print('Dezenda: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
