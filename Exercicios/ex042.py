print('{}-=-'.format('\033[34m') * 7)
print('Analisando Triângulos')
print('-=-' * 7)
n1 = float(input('{}Digite o 1º valor: '.format('\033[33m')))
n2 = float(input('Digite o 2º valor: '))
n3 = float(input('Digite o 3º valor: '))
if n1 + n2 > n3 and n2 + n3 > n1 and n3 + n1 > n2:
    print('{}Pode formar um triângulo '.format('\033[36m'), end='')
    if n1 == n2 == n3:
        print('EQUILÁTERO.')
    elif n1 == n2 or n2 == n3 or n3 == n1:
        print('ISÓCELES.')
    elif n1 != n2 != n3 != n1:
        print('ESCALENO.')
else:
    print('{}Não pode formar um triângulo.'.format('\033[31m'))
