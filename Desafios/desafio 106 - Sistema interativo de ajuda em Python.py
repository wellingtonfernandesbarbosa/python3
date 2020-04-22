def ajuda(x):
    print('\033[45m~' * 42)
    print(f'   Acessando o manual do comando {x}   ')
    print('~' * 42)
    print('\033[31;40m')
    help(f'{x}')


while True:
    print('\033[30;44m~' * 32)
    print(f'   Sistema de ajuda em PyHELP   ')
    print('~' * 32)
    r = str(input('\033[mFunção ou biblioteca > '))
    if r == 'fim':
        break
    ajuda(r)
print('\033[41m~' * 26)
print(f'{"ATÉ LOGO!":^26}')
print('~' * 26)
