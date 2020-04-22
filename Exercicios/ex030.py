print('{}='.format('\033[34m') * 20)
print('    PAR ou IMPAR')
print('=' * 20)
n = int(input('{}Digite um número: '.format('\033[32m')))
r = n % 2
if r == 0:
    print('{}O número {} é PAR.'.format('\033[36m',  n))
else:
    print('O número {} é IMPAR.'.format(n))
