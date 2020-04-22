print('{}='.format('\033[34m') * 48)
print(' ' * 14, 'Conversor de bases')
print('=' * 48)
i = int(input('{}Digite um número inteiro: '.format('\033[33m')))
print('Escolha uma das bases para a conversão:')
print('[ 1 ] converter  para  BINÁRIO\n[ 2 ] converter para OCTAL\n[ 3 ] converter para HEXADECIMAL')
c = int(input('Sua opção: '))
if c == 1:
    print('{}{} convertido para BINÁRIO é igual a {}.'.format('\033[36m', i, bin(i)[2:]))
elif c == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(i, oct(i)[2:]))
elif c == 3:
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(i, hex(i)[2:]))
else:
    print('{}Opção inválida. Tente novamente.'.format('\033[31m'))
