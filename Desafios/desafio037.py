print('Conversor de números')
n = int(input('Digite um número: '))
print('Para qual base deseja converte-lo? \n[ 1 ] para BINÁRIO \n[ 2 ] para OCTAL \n[ 3 ] para HEXADECIMAL ')
c = int(input('Sua opção: '))
if c == 1:
    print('{} Convertido para binário é igual a {}'.format(n, bin(n)[2:]))
elif c == 2:
    print('{} Convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif c == 3:
    print('{} Convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida. Tente novamente.')
