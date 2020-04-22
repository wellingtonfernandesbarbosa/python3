print('{}-=-'.format('\033[34m') * 9)
print('{}Maior e menor'.format(' ' * 7))
print('-=-' * 9)
n1 = int(input('{}Digite o primeiro valor: '.format('\033[33m')))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
me = n1
ma = n1
# Calculando o menor número
if me > n2:
    me = n2
if me > n3:
    me = n3
# Calculando o maior número
if ma < n2:
    ma = n2
if ma < n3:
    ma = n3
print('{}O menor número é {}.'.format('\33[36m', me))
print('O maior número é {}{}.'.format(ma, '\033[m'))
