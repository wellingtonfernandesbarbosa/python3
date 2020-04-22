n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))
me = n1
ma = n1
if me > n2:
    me = n2
if ma < n2:
    ma = n2
if me > n3:
    me = n3
if ma < n3:
    ma = n3
print('O menor número é {}'.format(me))
print('O maior número é {}'.format(ma))
