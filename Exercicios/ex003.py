print('{}-=-'.format('\033[32m') * 8)
print('    Somando números')
print('-=-' * 8)
n1 = int(input('{}Digite um numero: '.format('\033[33m')))
n2 = int(input('Digite um numero: '))
S = n1+n2
print('{}A soma entre {} e {} é {}.'.format('\033[34m', n1, n2, S))
