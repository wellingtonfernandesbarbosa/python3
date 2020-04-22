print('{}='.format('\033[34m') * 18)
print('Comparando números')
print('=' * 18)
n1 = int(input('{}Primeiro número: '.format('\033[33m')))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('{}O primeiro número é maior.'.format('\033[36m'))
elif n2 > n1:
    print('{}O segundo número é o maior.'.format('\033[36m'))
else:
    print('{}Os dois valores são IGUAIS.'.format('\033[35m'))
